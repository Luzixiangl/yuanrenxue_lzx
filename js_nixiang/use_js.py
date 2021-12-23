"""
    运行少量js代码建议使用该库
"""
import execjs

js_code = """
function func(a, b){
    return a+b
}
"""

result = execjs.compile(js_code).call('func', 2, 5)
print(result)