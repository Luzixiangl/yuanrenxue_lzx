"""
    请求规律检测：headers
    解：headers顺序不能乱，乱了就请求错误，因此采用session的方式，保证headers字典顺序不变
"""

import requests
import json

# session = requests.session()
# cookies = {
#     'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1636548155',
#     'no-alert': 'true',
#     'sessionid': '00baahlipy26jqhl4qnrslx4l50sk83c',
#     'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1638345172',
# }
#
# headers = {
#     'Host': 'www.python-spider.com',
#     'Connection': 'keep-alive',
#     'Content-Length': '6',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
#     'Origin': 'https://www.python-spider.com',
#     'Sec - Fetch - Site': 'same - origin',
#     'Sec - Fetch - Mode': 'cors',
#     'Sec - Fetch - Dest': 'empty',
#     'Referer': 'https://www.python-spider.com/challenge/10',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,und;q=0.6,ja;q=0.5',
# }
# session.headers = headers
#
# dataSum = 0
# for page in range(1, 2):
#     data = {
#       'page': str(page)
#     }
#
#     response = session.post('https://www.python-spider.com/api/challenge10', cookies=cookies, data=data, verify=False)
#     response_json = json.loads(response.text)
#     dataJson = response_json["data"]
#     for dataItem in dataJson:
#         cur_data = int(dataItem["value"])
#         dataSum += cur_data
# print("最终：", dataSum)



""" 修改成异步爬虫 """
import asyncio
import aiohttp
import cchardet

class Topic10Async:
    def __init__(self, name):
        self.dataSum = 0

        self._workers = 0
        self._workers_max = 10

        self.loop = asyncio.get_event_loop()  # 异步的事件循环
        self.queue = asyncio.Queue()
        self.session = aiohttp.ClientSession(loop=self.loop)  # aiohttp.ClientSession的对象，用于异步下载

        self.datajson_url = 'https://www.python-spider.com/api/challenge10'  # 数据api
        self._cookies = {
            'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1636548155',
            'no-alert': 'true',
            'sessionid': '00baahlipy26jqhl4qnrslx4l50sk83c',
            'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1638345172',
        }

        self._headers = {
            'Host': 'www.python-spider.com',
            'Connection': 'keep-alive',
            'Content-Length': '6',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://www.python-spider.com',
            'Sec - Fetch - Site': 'same - origin',
            'Sec - Fetch - Mode': 'cors',
            'Sec - Fetch - Dest': 'empty',
            'Referer': 'https://www.python-spider.com/challenge/10',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,und;q=0.6,ja;q=0.5',
        }

    async def loop_get_urls(self):
        """ 获取url """
        print("正在生成队列")
        for page in range(1, 101):
            await self.queue.put(page)
        print('queue 大小:', self.queue.qsize(), ', _workers:', self._workers)

    async def download(self, page, timeout=25):
        status_code = 900
        html = ''
        url_now = self.datajson_url
        data = {
            'page': str(page)
        }
        try:
            # 再获取数据接口
            async with self.session.post(url_now, headers=self._headers, cookies=self._cookies,
                                         timeout=timeout, data=data) as response:
                status_code = response.status
                html = await response.read()
                encoding = cchardet.detect(html)['encoding']
                html = html.decode(encoding, errors='ignore')
                url_now = str(response.url)
        except Exception as e:
            print("==== 异常：", e, type(e), str(e))
            msg = 'Failed download: {} | exception: {}, {}'.format(page, str(type(e)), str(e))
            print(msg)
        return status_code, html, url_now

    async def process(self, page):
        status, html, url_now = await self.download(page)
        self._workers -= 1
        print('已下载:', page, ', html:', len(html))
        try:
            dataJson = json.loads(html)["data"]
            for dataItem in dataJson:
                cur_data = int(dataItem["value"])
                self.dataSum += cur_data
            print("self.dataSum结果：", self.dataSum)
        except Exception as e:
            print("==== 数据处理异常：", e, type(e), str(e))
            msg = 'Failed download: {} | exception: {}, {}, html:{}'.format(page, str(type(e)), str(e), html)
            print(msg)

    async def loop_crawl(self):
        print("----------- 启动 --------------")
        asyncio.ensure_future(self.loop_get_urls())
        counter = 0
        # while 1:
        #     if self.queue.qsize() != 0:
        #         continue
        while 1:
            print("------- go --------")
            page = await self.queue.get()  # 从queue队列中获取urls
            self._workers += 1
            counter += 1
            asyncio.ensure_future(self.process(page))
            print("----------- 本次挂起 --------------, self._workers: ", self._workers)
            if self._workers > self._workers_max:
                print(" --------- _workers大于设定的值，先休息三秒 ---------")
                await asyncio.sleep(3)
    def run(self):
        try:
            self.loop.run_until_complete(self.loop_crawl())
        except KeyboardInterrupt:
            print('自己停下来的！')


if __name__ == '__main__':
    # 正确答案：5113761
    nc = Topic10Async('yrx-async')
    nc.run()