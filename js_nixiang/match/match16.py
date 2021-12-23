import requests
import execjs
import time

cookies = {
    'sessionid': 'ufzxafi6h4gori7pgvorfmi6udhgqcr7'

}

headers = {
    'User-Agent': 'yuanrenxue.project',
}

with open('match16.js', 'r', encoding='utf-8') as f:
    js_text = f.read()
    compile = execjs.compile(js_text)

num = 0
for page in range(1, 6):
    result_time = str(int(time.time() * 1000))
    result_m = compile.call('MATCH_SDK_16', result_time)

    params = (
        ('page', str(page)),
        ('m', result_m),
        ('t', result_time),
    )

    response = requests.get('https://match.yuanrenxue.com/api/match/16', headers=headers, params=params, cookies=cookies)
    print(response.text)
    for data in response.json()['data']:
        num += data['value']
print(num)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://match.yuanrenxue.com/api/match/16?page=2&m=zknWHBTjmsh4zH8794f6794d31eec4e7de57356847f4fd2J5ktZYRDF6&t=1640059445000', headers=headers, cookies=cookies)
