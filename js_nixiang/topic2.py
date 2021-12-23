"""
    cookie加密：抠代码
"""

import requests
import execjs
session = requests.session()
cookies = {
    'sessionid': 'pxu79y1nd8zmneatfv4hwlrfy3odtjhq'
}

with open('topic2.js', 'r', encoding='utf-8') as f:
    js_text = f.read()
    compile = execjs.compile(js_text)
    cookies['sign'] = compile.call('SDK_2').split(';')[0].replace('sign=', '')
response = session.get('https://www.python-spider.com/challenge/2', cookies=cookies)

print(response.content.decode())