"""
    简单的js补环境
"""

import requests
import execjs
import re
from lxml import etree

session = requests.session()
cookies = {
    'sessionid': 'hj454xb2nw3158q8cot2gzzhooasuu46',
}

res = session.get('https://www.python-spider.com/challenge/11', cookies=cookies)
js_text = re.match('<script>(.*)</script>', res.content.decode()).group(1)
js_text = '''
function SDK_11() {

    setTimeout = function () {
    };
    location = {};
    location.pathname = '/challenge/11';
    location.search = "";

    document = {};
    document.cookie = "";
    document.createElement = function () {
        return {
            innerHTML: "",
            firstChild: {
                href: 'https://www.python-spider.com/',
            }
        }
    };
    window = global;
    window.addEventListener = function () {
    };

    document.addEventListener = function (a, b, c) {
        b()
    };
    document.attachEvent = function () {
    };
''' + js_text + '''
    return document.cookie
}
'''

compile = execjs.compile(js_text)
token_split = compile.call('SDK_11').split('=')
print(token_split)

cookies = {
    'sessionid': 'hj454xb2nw3158q8cot2gzzhooasuu46',
    token_split[0]: token_split[1].split(';')[0]
}

res = requests.get(url='https://www.python-spider.com/challenge/11', cookies=cookies)
print(res.text)
html = etree.HTML(res.text)

num = 0
for data in html.xpath("//table/tr/td/text()"):
    num += int(data)
print(num)