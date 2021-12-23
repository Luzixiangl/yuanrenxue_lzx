#!/usr/bin/env python3
# Author: veelion
"""
    同步抓取
"""

import urllib.parse as urlparse
import lzma
import farmhash
import traceback


from ezpymysql import Connection
from urlpool import UrlPool
import functions as fn
import config

class NewsCrawlerSync:
    def __init__(self, name):
        # 初始化数据库
        self.db = Connection(
            config.db_host,
            config.db_db,
            config.db_user,
            config.db_password
        )
        # 初始化logger
        self.logger = fn.init_file_logger(name + '.log')
        # 实现网址池
        self.urlpool = UrlPool(name)
        self.hub_hosts = None
        self.load_hubs()

    def load_hubs(self,):
        """ 访问mysql数据表，加载hub url """
        sql = 'select url from crawler_hub'
        data = self.db.query(sql)
        self.hub_hosts = set()
        hubs = []
        for d in data:
            host = urlparse.urlparse(d['url']).netloc
            self.hub_hosts.add(host)
            hubs.append(d['url'])
        # 设置为每隔5分钟需要爬一次
        self.urlpool.set_hubs(hubs, 300)

    def save_to_db(self, url, html):
        print("url:", url)
        # 将url、html保存在数据库
        urlhash = farmhash.hash64(url)
        sql = 'select url from crawler_html where urlhash=%s'
        d = self.db.get(sql, urlhash)
        if d:
            if d['url'] != url:
                msg = 'farmhash 冲突: %s <=> %s' % (url, d['url'])
                self.logger.error(msg)
            return True
        if isinstance(html, str):
            html = html.encode('utf8')
        # 压缩html
        html_lzma = lzma.compress(html)
        sql = ('insert into crawler_html(urlhash, url, html_lzma) '
               'values(%s, %s, %s)')
        good = False
        try:
            self.db.execute(sql, urlhash, url, html_lzma)
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
        """ 对url过滤，筛选需要爬取的url"""
        goodlinks = []
        for url in urls:
            host = urlparse.urlparse(url).netloc
            if host in self.hub_hosts:
                goodlinks.append(url)
        return goodlinks

    def process(self, url, ishub):
        """ 处理url """
        status, html, redirected_url = fn.downloader(url)
        # 提交响应状态
        self.urlpool.set_status(url, status)

        if redirected_url != url:
            self.urlpool.set_status(redirected_url, status)
        # 提取hub网页中的链接, 新闻网页中也有“相关新闻”的链接，按需提取
        if status != 200:
            return
        if ishub:
            # 获取hub url 里的新链接
            newlinks = fn.extract_links_re(redirected_url, html)
            goodlinks = self.filter_good(newlinks)
            print("%s/%s, goodlinks/newlinks" % (len(goodlinks), len(newlinks)))
            self.urlpool.addmany(goodlinks)
        else:
            self.save_to_db(redirected_url, html)

    def run(self,):
        while 1:
            urls = self.urlpool.pop(5)
            print("urls：", urls)
            input("暂停")
            for url, ishub in urls.items():
                self.process(url, ishub)


if __name__ == '__main__':
    crawler = NewsCrawlerSync('yuanrenxyue')
    crawler.run()
