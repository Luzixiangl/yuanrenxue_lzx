"""
    第一题：简单的参数加密
"""
import base64
import hashlib
import requests
import time
import datetime
import re

cookies = {
    'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d': '1636548155',
    'no-alert': 'true',
    'sessionid': 's51opkeefakukf6fn2vmdn0oks7t736n',
    'Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d': '1638193304',
}


def get_headers():
    now_date = str(int(time.time()))
    b_safe_value = base64.b64encode(b"9622" + bytes(now_date, encoding='utf-8'))
    m = hashlib.md5()
    m.update(b_safe_value)
    md5_safe_value = m.hexdigest()
    print(now_date)
    print(b_safe_value)
    print(md5_safe_value)
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'timestamp': now_date,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'safe': md5_safe_value,
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.python-spider.com/challenge/1',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,und;q=0.6,ja;q=0.5',
    }
    return headers

count = 0
for page in range(1, 86):
    now_headers = get_headers()
    response = requests.get('https://www.python-spider.com/challenge/api/json?page={page}&count=14'.format(page=page), headers=now_headers, cookies=cookies)
    print(response.text)
    for data in response.json()['infos']:
        if '招' in data['message']:
            count += 1
            print(data['message'])
print('最终结果：', count)

