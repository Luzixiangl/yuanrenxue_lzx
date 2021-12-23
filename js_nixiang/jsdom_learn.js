// 导入jsdom
const jsdom = require('jsdom');
// 生成jsdom对象  jsdom实例化，等价于：JSDOM = jsdom.JSDOM;
const {JSDOM} = jsdom;
// 倒入读写js的包
const fs = require('fs');

options = {
    url: "http://match.yuanrenxue.com/match/2",
    referrer: "http://match.yuanrenxue.com/match/2",
    contentType: "text/html",
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    includeNodeLocations: true,
    runScripts: 'dangerously',

    cookieJar: new jsdom.CookieJar(),
    beforeParse(window) {
        // window.alert();
        window.setInterval = function (s, b) {
            eval(s)
        };
        //重写之后进行伪装
        window.setInterval.toString = function () {
            "function setInterval() { [native code] }"
        };
        window.setTimeout = function (s, b) {
            eval(s)
        };
        window.setTimeout.toString = function () {
            "function setTimeout() { [native code] }"
        }
    },

};
// 提前植入setcookie的操作
// options.cookieJar.setCookie(cookie, url, function (val) {
// });
// 对1.html进行对去操作
fs.readFile('./match/match_2_sy', 'utf8', function (err, data) {
    //定制jsdom，data一般是js代码，由于安全策略的原因导致无法自动加载script标签
    //需要开启安全策略的开关，runScripts: "dangerously"
    //js代码直接写入会报错。所以一般在本地新建个html文件，像刚刚的1。html，然后用fs.readFile进行读取操作
    const dom = new JSDOM(data
        ,
        options
    );
    console.log('cookie结果为：', dom.window.document);
    console.log('cookie结果为：', dom.window.document.cookie);
    //将dom窗口关闭
    dom.window.close()
});