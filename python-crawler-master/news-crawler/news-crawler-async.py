#!/usr/bin/env python3
# File: news-crawler-async.py
# Author: veelion
"""
    异步爬虫

"""

import traceback
import time
import asyncio
import aiohttp
import urllib.parse as urlparse
import farmhash
import lzma
import json

# uvloop是C语言实现的高性能异步I/O库，用uvloop替代asyncio自己的事件循环可以使asyncio的速度更快，甚至接近于Go语言的性能（window该包不支持）
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

import sanicdb  # aiomysql的封装

from urlpool import UrlPool
import functions as fn
import config


class NewsCrawlerAsync:
    def __init__(self, name):
        self.stop = 0           # 初始化程序退出标志
        self._workers = 0       # 计数器，记录当前生成下载url的协程
        self._workers_max = 30  # 限制爬虫最多生成下载url的协程。取决于CPU和带宽，运行中自己调试出最佳理想值
        self.logger = fn.init_file_logger(name + '.log')

        self.urlpool = UrlPool(name)    # 网址池

        self.loop = asyncio.get_event_loop()    # 异步的事件循环
        self.session = aiohttp.ClientSession(loop=self.loop)    # aiohttp.ClientSession的对象，用于异步下载
        self.db = sanicdb.SanicDB(
            config.db_host,
            config.db_db,
            config.db_user,
            config.db_password,
            loop=self.loop
        )

    def __del__(self):
        """
            优雅的退出程序
        :return:
        """
        self.stop = 1

    """
        函数方法，内部需要IO操作的，那么该函数就声明为async作为协程函数，否则不声明
    """

    async def load_hubs(self,):
        # 将hub url 放入网址池里头
        sql = 'select url from crawler_hub'
        data = await self.db.query(sql)     # 读取mysql即添加await
        self.hub_hosts = set()
        hubs = []
        for d in data:
            host = urlparse.urlparse(d['url']).netloc
            self.hub_hosts.add(host)
            hubs.append(d['url'])
        self.urlpool.set_hubs(hubs, 300)

    async def save_to_db(self, url, html):
        urlhash = farmhash.hash64(url)
        sql = 'select url from crawler_html where urlhash=%s'
        d = await self.db.get(sql, urlhash)     # 读数据库
        if d:
            if d['url'] != url:
                msg = 'farmhash 冲突: %s <=> %s' % (url, d['url'])
                self.logger.error(msg)
            return True
        if isinstance(html, str):
            html = html.encode('utf8')
        html_lzma = lzma.compress(html)
        sql = ('insert into crawler_html(urlhash, url, html_lzma) '
               'values(%s, %s, %s)')
        good = False
        try:
            await self.db.execute(sql, urlhash, url, html_lzma)
            good = True
        except Exception as e:
            if e.args[0] == 1062:
                # Duplicate entry
                good = True
                pass
            else:
                traceback.print_exc()
                raise e
        return good

    def filter_good(self, urls):
        # 判断url是否是我们想访问的，整个过程仅涉及cpu计算，因此不需要异步协程
        goodlinks = []
        for url in urls:
            host = urlparse.urlparse(url).netloc
            if host in self.hub_hosts:
                goodlinks.append(url)
        return goodlinks

    async def process(self, url, ishub):
        # 处理url的过程
        status, html, redirected_url = await fn.fetch(self.session, url)    # 先下载url，得到响应
        self.urlpool.set_status(url, status)
        if redirected_url != url:
            self.urlpool.set_status(redirected_url, status)
        # 提取hub网页中的链接, 新闻网页中也有“相关新闻”的链接，按需提取
        if status != 200:
            self._workers -= 1
            return
        if ishub:
            newlinks = fn.extract_links_re(redirected_url, html)
            goodlinks = self.filter_good(newlinks)
            print("%s/%s, 好的链接/新链接" % (len(goodlinks), len(newlinks)))
            self.urlpool.addmany(goodlinks)
        else:
            await self.save_to_db(redirected_url, html)
        self._workers -= 1
        print("当前worker处理完成，释放该worker,释放后，self._worker为", self._workers)

    def load_config(self):

        """
        加载配置文件
        文件：json {
            'a': 3,
            'b': 4,
            'stop': 1,
        }
        :return:
        """
        with open('conf-news-crawler-async.json', 'r') as f:
            conf_dict = json.loads(f.read())
        return conf_dict

    async def loop_crawl(self,):
        # 相当于爬虫main函数的主循环
        await self.load_hubs()
        last_rating_time = time.time()
        counter = 0     # 计数器
        last_load = time.time()
        while 1:
            if time.time() - last_load > 13:   # 每隔10秒读取一次配置文件
                config_dict = self.load_config()
                last_load = time.time()
                self.stop = config_dict['stop']
            if self.stop:       # 优雅的退出程序
                print("即将退出，请稍等，检测当前未关闭容器为：", self._workers)
                while self._workers > 0:
                    print("正在等待未关闭容器完成任务，当前未关闭容器：", self._workers)
                    await asyncio.sleep(1)
                break
            to_pop = self._workers_max - self._workers
            tasks = self.urlpool.pop(to_pop)
            if not tasks:
                print('没有可抓取的网址，休眠')
                await asyncio.sleep(3)
                continue
            for url, ishub in tasks.items():
                self._workers += 1
                counter += 1
                print('crawl:', url)
                asyncio.ensure_future(self.process(url, ishub))

            # 每隔一段时间打印爬虫信息
            gap = time.time() - last_rating_time
            if gap > 5:
                rate = counter / gap
                print('\tloop_crawl() 速度:%s, 计数器: %s, workers: %s' % (round(rate, 2), counter, self._workers))
                last_rating_time = time.time()
                counter = 0

            if self._workers >= self._workers_max:
                print('====== 达到 workers_max 瓶颈, 先休息3秒再尝试运行下一个worker =====')
                await asyncio.sleep(3)
            else:
                print('未达到瓶颈，当前_workers为：', self._workers)

    def run(self):
        try:
            self.loop.run_until_complete(self.loop_crawl())
        except KeyboardInterrupt:
            print('自己停下来的！')
            del self.urlpool


if __name__ == '__main__':
    nc = NewsCrawlerAsync('yrx-async')
    nc.run()
    # print(nc.load_config())


