import base64
import requests

print(base64.b64encode(b"yuanrenxue1"), type(base64.b64encode(b"yuanrenxue1")))     # 编码
print(str(base64.b64encode(b"yuanrenxue1"), encoding='utf-8'), type(str(base64.b64encode(b"yuanrenxue1"), encoding='utf-8')))
b_m = base64.b64encode(b"yuanrenxue" + bytes('1', encoding='utf-8'))
print('!!!!!', b_m, type(b_m))
print('??????', str(b_m, encoding='utf-8'), type(str(b_m, encoding='utf-8')))

cookies = {
    'Hm_lvt_c99546cf032aaa5a679230de9a95c7db': '1639143180',
    'no-alert3': 'true',
    'Hm_lvt_9bcbda9cbf86757998a2339a0437208e': '1639204397',
    'Hm_lvt_0362c7a08a9a04ccf3a8463c590e1e2f': '1639054053,1639204441',
    'Hm_lpvt_0362c7a08a9a04ccf3a8463c590e1e2f': '1639204441',
    'sessionid': 'o8hyl2f13k9ucn85t6ysbrv9vfmgkxat',
    'Hm_lpvt_9bcbda9cbf86757998a2339a0437208e': '1639212268',
    'Hm_lpvt_c99546cf032aaa5a679230de9a95c7db': '1639212268',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'yuanrenxue.project',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://match.yuanrenxue.com/match/12',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,und;q=0.6,ja;q=0.5',
}

def get_params(page):
    b_m_value = base64.b64encode(b"yuanrenxue" + bytes(page, encoding='utf-8'))
    params = (
        ('page', page),
        ('m', str(b_m_value, encoding='utf-8'))
    )
    return params

sum_value = 0
for page in range(1, 6):
    print("页数：", page)
    response = requests.get('https://match.yuanrenxue.com/api/match/12', headers=headers, params=get_params(str(page)), cookies=cookies)
    datas = response.json()['data']
    for data in datas:
        sum_value += data['value']
print('最终结果', sum_value)
