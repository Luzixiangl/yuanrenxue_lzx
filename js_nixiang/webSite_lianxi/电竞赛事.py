"""
    解析：https://mp.weixin.qq.com/s/FZ8gR6dKCSpBajaTG_NEww

    目前：无法断点到请求，找到cp的加密函数
"""

import requests

cookies = {
    'VPLang': 'zh_CN',
    'gr_user_id': '1494a435-7a59-4fbd-9b77-779a614844a2',
    'grwng_uid': '36dd1101-97d6-4a6b-b8cd-76c8bf5312a0',
    '__auc': 'd0873a4717d4714d668cc6cb026',
    'VPLang.sig': 'YnJ5rF9PQgOnWLVHGcoeKlgoy3E',
    'bd6e328645187581_gr_session_id': '36eeccc3-fc07-4e7c-812c-d18f29b3db3f',
    'Hm_lvt_20c4cdf230856f4a4479a32ec8b13dd6': '1637575088,1639968261',
    '__asc': 'fc58e5e017dd5b9c385b0675fa6',
    'Device-Id': '0312b7d0286fcc44d71a237dd4a24947',
    'Device-Id.sig': 'lFPqbwc7yaTRG_QlIXCTWC9I4mg',
    'bd6e328645187581_gr_session_id_36eeccc3-fc07-4e7c-812c-d18f29b3db3f': 'true',
    'VPSiteGame': 'lol',
    'VPSiteGame.sig': 'JqpHYiVdDwyf5WcBoCAreVVDpkI',
    'Hm_lpvt_20c4cdf230856f4a4479a32ec8b13dd6': '1639968528',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.vpgame.com/schedule',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,pt;q=0.7,und;q=0.6,ja;q=0.5',
}

params = (
    ('', ''),
    ('game_type', 'lol'),
    ('start_date', '1627747200'),
    ('end_date', '1635696000'),
    ('status', 'end'),
    ('as', '1639987045310'),
    ('cp', '2fc4abcd559a53e2ffcea72cd64a033d'),
    ('t', '1639969385359'),
)

response = requests.get('https://www.vpgame.com/schedule/sha/dota2/pro/webservice/schedule/list/all', headers=headers, params=params, cookies=cookies, verify=False)
print(response.text)
