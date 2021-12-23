"""
    简单的cookies
"""
import requests
import re
import execjs

session = requests.session()
h = {
    'User-Agent': 'yuanrenxue.project',
    'cookie': 'sessionid=o8hyl2f13k9ucn85t6ysbrv9vfmgkxat'
}
index_response = session.get('https://match.yuanrenxue.com/match/13', headers=h)
# 构造要执行的js代码
js_code = f'''
document = new Object();
location = new Object();
function result(){{
    {re.match('<script>(.*)</script>', index_response.content.decode()).group(1)};
    return document.cookie
}}
'''
cookie = str(execjs.compile(js_code).call('result'))
print('获取计算出来的cookie为：', cookie)


cookies = {
    'sessionid': 'o8hyl2f13k9ucn85t6ysbrv9vfmgkxat',
    cookie.split('=')[0]: cookie.split('=')[1].split(';')[0],
}

print('最终cookies', cookies)
headers = {
    'User-Agent': 'yuanrenxue.project',
    # 'cookie': 'sessionid=o8hyl2f13k9ucn85t6ysbrv9vfmgkxat;{}'.format(cookie.split(';')[0])
}
sum_value = 0
print(headers)
for page in range(1, 6):
    response = session.get('https://match.yuanrenxue.com/api/match/13?page=' + str(page), headers=headers, cookies=cookies)
    print(response.text)
    datas = response.json()['data']
    for data in datas:
        sum_value += data['value']
print('最终结果', sum_value)
