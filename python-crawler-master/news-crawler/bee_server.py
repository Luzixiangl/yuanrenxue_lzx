#!/usr/bin/env python3
# encoding: utf8
# author: veelion
# file: bee_server.py

from sanic import Sanic
from sanic import response

from urlpool import UrlPool

urlpool = UrlPool(__file__)

# 初始化urlpool，根据你的需要进行修改
hub_urls = []
urlpool.set_hubs(hub_urls, 300)
urlpool.add('https://news.sina.com.cn/')

# init
app = Sanic(__name__)

# web server停止时运行. 在Server退出前，缓存URLPool里面的url。
@app.listener('after_server_stop')
async def cache_urlpool(app, loop):
    global urlpool
    print('caching urlpool after_server_stop')
    del urlpool
    print('bye!')

# client端获取urls
@app.route('/task')
async def task_get(request):
    count = request.args.get('count', 10)
    try:
        count = int(count)
    except:
        count = 10
    urls = urlpool.pop(count)
    return response.json(urls)

# client端提交urls的结果
@app.route('/task', methods=['POST', ])
async def task_post(request):
    result = request.json
    urlpool.set_status(result['url'], result['status'])
    if result['url_real'] != result['url']:
        urlpool.set_status(result['url_real'], result['status'])
    if result['newurls']:
        print('receive URLs:', len(result['newurls']))
        for url in result['newurls']:
            urlpool.add(url)
    return response.text('ok')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=False,
        access_log=False,
        workers=1)

