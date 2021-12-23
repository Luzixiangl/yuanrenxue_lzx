"""
    window 蜜罐
"""


import requests
import execjs


cookies = {
    'sessionid': 'hj454xb2nw3158q8cot2gzzhooasuu46',
}

headers = {
    'safe': ''
}

with open('topic16.js', 'r', encoding='gbk') as f:
    js_text = f.read()

num = 0
for page in range(1, 101):
    compile = execjs.compile(js_text)
    headers['safe'] = compile.call('SDK_16')
    print('第', page, '页：', headers['safe'])

    data = {
      'page': str(page)
    }

    response = requests.post('https://www.python-spider.com/api/challenge16', headers=headers, cookies=cookies, data=data)

    for d in response.json()['data']:
        num += int(d['value'])
print(num)
