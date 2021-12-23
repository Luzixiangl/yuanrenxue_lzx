window = global;

(window.__LOADABLE_LOADED_CHUNKS__ = window.__LOADABLE_LOADED_CHUNKS__ || []).push([[8], {
    aCH8: function (e, t, n) {
        !function () {
            var t = n("ANhw")
                , r = n("mmNF").utf8
                , o = n("BEtg")
                , i = n("mmNF").bin
                , a = function (e, n) {
                e.constructor == String ? e = n && "binary" === n.encoding ? i.stringToBytes(e) : r.stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || (e = e.toString());
                for (var c = t.bytesToWords(e), u = 8 * e.length, l = 1732584193, s = -271733879, f = -1732584194, h = 271733878, d = 0; d < c.length; d++)
                    c[d] = 16711935 & (c[d] << 8 | c[d] >>> 24) | 4278255360 & (c[d] << 24 | c[d] >>> 8);
                c[u >>> 5] |= 128 << u % 32,
                    c[14 + (u + 64 >>> 9 << 4)] = u;
                var p = a._ff
                    , v = a._gg
                    , m = a._hh
                    , g = a._ii;
                for (d = 0; d < c.length; d += 16) {
                    var y = l
                        , b = s
                        , w = f
                        , M = h;
                    l = p(l, s, f, h, c[d + 0], 7, -680876936),
                        h = p(h, l, s, f, c[d + 1], 12, -389564586),
                        f = p(f, h, l, s, c[d + 2], 17, 606105819),
                        s = p(s, f, h, l, c[d + 3], 22, -1044525330),
                        l = p(l, s, f, h, c[d + 4], 7, -176418897),
                        h = p(h, l, s, f, c[d + 5], 12, 1200080426),
                        f = p(f, h, l, s, c[d + 6], 17, -1473231341),
                        s = p(s, f, h, l, c[d + 7], 22, -45705983),
                        l = p(l, s, f, h, c[d + 8], 7, 1770035416),
                        h = p(h, l, s, f, c[d + 9], 12, -1958414417),
                        f = p(f, h, l, s, c[d + 10], 17, -42063),
                        s = p(s, f, h, l, c[d + 11], 22, -1990404162),
                        l = p(l, s, f, h, c[d + 12], 7, 1804603682),
                        h = p(h, l, s, f, c[d + 13], 12, -40341101),
                        f = p(f, h, l, s, c[d + 14], 17, -1502002290),
                        l = v(l, s = p(s, f, h, l, c[d + 15], 22, 1236535329), f, h, c[d + 1], 5, -165796510),
                        h = v(h, l, s, f, c[d + 6], 9, -1069501632),
                        f = v(f, h, l, s, c[d + 11], 14, 643717713),
                        s = v(s, f, h, l, c[d + 0], 20, -373897302),
                        l = v(l, s, f, h, c[d + 5], 5, -701558691),
                        h = v(h, l, s, f, c[d + 10], 9, 38016083),
                        f = v(f, h, l, s, c[d + 15], 14, -660478335),
                        s = v(s, f, h, l, c[d + 4], 20, -405537848),
                        l = v(l, s, f, h, c[d + 9], 5, 568446438),
                        h = v(h, l, s, f, c[d + 14], 9, -1019803690),
                        f = v(f, h, l, s, c[d + 3], 14, -187363961),
                        s = v(s, f, h, l, c[d + 8], 20, 1163531501),
                        l = v(l, s, f, h, c[d + 13], 5, -1444681467),
                        h = v(h, l, s, f, c[d + 2], 9, -51403784),
                        f = v(f, h, l, s, c[d + 7], 14, 1735328473),
                        l = m(l, s = v(s, f, h, l, c[d + 12], 20, -1926607734), f, h, c[d + 5], 4, -378558),
                        h = m(h, l, s, f, c[d + 8], 11, -2022574463),
                        f = m(f, h, l, s, c[d + 11], 16, 1839030562),
                        s = m(s, f, h, l, c[d + 14], 23, -35309556),
                        l = m(l, s, f, h, c[d + 1], 4, -1530992060),
                        h = m(h, l, s, f, c[d + 4], 11, 1272893353),
                        f = m(f, h, l, s, c[d + 7], 16, -155497632),
                        s = m(s, f, h, l, c[d + 10], 23, -1094730640),
                        l = m(l, s, f, h, c[d + 13], 4, 681279174),
                        h = m(h, l, s, f, c[d + 0], 11, -358537222),
                        f = m(f, h, l, s, c[d + 3], 16, -722521979),
                        s = m(s, f, h, l, c[d + 6], 23, 76029189),
                        l = m(l, s, f, h, c[d + 9], 4, -640364487),
                        h = m(h, l, s, f, c[d + 12], 11, -421815835),
                        f = m(f, h, l, s, c[d + 15], 16, 530742520),
                        l = g(l, s = m(s, f, h, l, c[d + 2], 23, -995338651), f, h, c[d + 0], 6, -198630844),
                        h = g(h, l, s, f, c[d + 7], 10, 1126891415),
                        f = g(f, h, l, s, c[d + 14], 15, -1416354905),
                        s = g(s, f, h, l, c[d + 5], 21, -57434055),
                        l = g(l, s, f, h, c[d + 12], 6, 1700485571),
                        h = g(h, l, s, f, c[d + 3], 10, -1894986606),
                        f = g(f, h, l, s, c[d + 10], 15, -1051523),
                        s = g(s, f, h, l, c[d + 1], 21, -2054922799),
                        l = g(l, s, f, h, c[d + 8], 6, 1873313359),
                        h = g(h, l, s, f, c[d + 15], 10, -30611744),
                        f = g(f, h, l, s, c[d + 6], 15, -1560198380),
                        s = g(s, f, h, l, c[d + 13], 21, 1309151649),
                        l = g(l, s, f, h, c[d + 4], 6, -145523070),
                        h = g(h, l, s, f, c[d + 11], 10, -1120210379),
                        f = g(f, h, l, s, c[d + 2], 15, 718787259),
                        s = g(s, f, h, l, c[d + 9], 21, -343485551),
                        l = l + y >>> 0,
                        s = s + b >>> 0,
                        f = f + w >>> 0,
                        h = h + M >>> 0
                }
                return t.endian([l, s, f, h])
            };
            a._ff = function (e, t, n, r, o, i, a) {
                var c = e + (t & n | ~t & r) + (o >>> 0) + a;
                return (c << i | c >>> 32 - i) + t
            }
                ,
                a._gg = function (e, t, n, r, o, i, a) {
                    var c = e + (t & r | n & ~r) + (o >>> 0) + a;
                    return (c << i | c >>> 32 - i) + t
                }
                ,
                a._hh = function (e, t, n, r, o, i, a) {
                    var c = e + (t ^ n ^ r) + (o >>> 0) + a;
                    return (c << i | c >>> 32 - i) + t
                }
                ,
                a._ii = function (e, t, n, r, o, i, a) {
                    var c = e + (n ^ (t | ~r)) + (o >>> 0) + a;
                    return (c << i | c >>> 32 - i) + t
                }
                ,
                a._blocksize = 16,
                a._digestsize = 16,
                e.exports = function (e, n) {
                    if (void 0 === e || null === e)
                        throw new Error("Illegal argument " + e);
                    var r = t.wordsToBytes(a(e, n));
                    return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r)
                }
        }()
    },
    ANhw: function (e, t) {
        !function () {
            var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", n = {
                rotl: function (e, t) {
                    return e << t | e >>> 32 - t
                }, rotr: function (e, t) {
                    return e << 32 - t | e >>> t
                }, endian: function (e) {
                    if (e.constructor == Number) return 16711935 & n.rotl(e, 8) | 4278255360 & n.rotl(e, 24);
                    for (var t = 0; t < e.length; t++) e[t] = n.endian(e[t]);
                    return e
                }, randomBytes: function (e) {
                    for (var t = []; e > 0; e--) t.push(Math.floor(256 * Math.random()));
                    return t
                }, bytesToWords: function (e) {
                    for (var t = [], n = 0, r = 0; n < e.length; n++, r += 8) t[r >>> 5] |= e[n] << 24 - r % 32;
                    return t
                }, wordsToBytes: function (e) {
                    for (var t = [], n = 0; n < 32 * e.length; n += 8) t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
                    return t
                }, bytesToHex: function (e) {
                    for (var t = [], n = 0; n < e.length; n++) t.push((e[n] >>> 4).toString(16)), t.push((15 & e[n]).toString(16));
                    return t.join("")
                }, hexToBytes: function (e) {
                    for (var t = [], n = 0; n < e.length; n += 2) t.push(parseInt(e.substr(n, 2), 16));
                    return t
                }, bytesToBase64: function (e) {
                    for (var n = [], r = 0; r < e.length; r += 3) for (var o = e[r] << 16 | e[r + 1] << 8 | e[r + 2], i = 0; i < 4; i++) 8 * r + 6 * i <= 8 * e.length ? n.push(t.charAt(o >>> 6 * (3 - i) & 63)) : n.push("=");
                    return n.join("")
                }, base64ToBytes: function (e) {
                    e = e.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var n = [], r = 0, o = 0; r < e.length; o = ++r % 4) 0 != o && n.push((t.indexOf(e.charAt(r - 1)) & Math.pow(2, -2 * o + 8) - 1) << 2 * o | t.indexOf(e.charAt(r)) >>> 6 - 2 * o);
                    return n
                }
            };
            e.exports = n
        }()
    },
    mmNF: function (e, t) {
        var n = {
            utf8: {
                stringToBytes: function (e) {
                    return n.bin.stringToBytes(unescape(encodeURIComponent(e)))
                },
                bytesToString: function (e) {
                    return decodeURIComponent(escape(n.bin.bytesToString(e)))
                }
            },
            bin: {
                stringToBytes: function (e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(255 & e.charCodeAt(n));
                    return t
                },
                bytesToString: function (e) {
                    for (var t = [], n = 0; n < e.length; n++)
                        t.push(String.fromCharCode(e[n]));
                    return t.join("")
                }
            }
        };
        e.exports = n
    },
    BEtg: function (e, t) {
        function n(e) {
            return !!e.constructor && "function" === typeof e.constructor.isBuffer && e.constructor.isBuffer(e)
        }

        e.exports = function (e) {
            return null != e && (n(e) || function (e) {
                return "function" === typeof e.readFloatLE && "function" === typeof e.slice && n(e.slice(0, 0))
            }(e) || !!e._isBuffer)
        }
    },
}, [[0, 19, 0, 20]]]);

!function(e) {
   function t(t) {
        for (var r, n, l = t[0], u = t[1], c = t[2], s = 0, g = []; s < l.length; s++)
            n = l[s],
            a[n] && g.push(a[n][0]),
                a[n] = 0;
        for (r in u)
            Object.prototype.hasOwnProperty.call(u, r) && (e[r] = u[r]);
        for (d && d(t); g.length;)
            g.shift()();
        return i.push.apply(i, c || []),
            o()
    }

    function o() {
        for (var e, t = 0; t < i.length; t++) {
            for (var o = i[t], r = !0, n = 1; n < o.length; n++) {
                var u = o[n];
                0 !== a[u] && (r = !1)
            }
            r && (i.splice(t--, 1),
                e = l(l.s = o[0]))
        }
        return e
    }

    var r = {}
        , n = {
        19: 0
    }
        , a = {
        19: 0
    }
        , i = [];

    function l(t) {
        console.log(t)
        if (r[t])
            return r[t].exports;
        var o = r[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(o.exports, o, o.exports, l),
            o.l = !0,
            o.exports
    }

    l.e = function (e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1
        }[e] && t.push(n[e] = new Promise((function (t, o) {
                for (var r = "css/" + ({
                    1: "vendors~csgoLive~dota2Live~index~league~leagueLol~leaugeVa~lolLive",
                    2: "vendors~csgoLive~dota2Live~index~lolLive~owlive~pubglive",
                    3: "vendors~LeagueCsgo~dota2Live~index~league~lolLive",
                    4: "LeagueCsgo~leaugeVa",
                    5: "csgoLive~owlive~pubglive",
                    6: "leaugeVa",
                    7: "LeagueCsgo",
                    9: "csgoLive",
                    10: "dota2Live",
                    11: "index",
                    12: "league",
                    13: "leagueLol",
                    14: "lolLive",
                    15: "match10",
                    16: "notfound",
                    17: "owlive",
                    18: "pubglive"
                }[e] || e) + ".f2ebe51677ffeebc6745.webp.css", a = l.p + r, i = document.getElementsByTagName("link"), u = 0; u < i.length; u++) {
                    var c = (d = i[u]).getAttribute("data-href") || d.getAttribute("href");
                    if ("stylesheet" === d.rel && (c === r || c === a))
                        return t()
                }
                var s = document.getElementsByTagName("style");
                for (u = 0; u < s.length; u++) {
                    var d;
                    if ((c = (d = s[u]).getAttribute("data-href")) === r || c === a)
                        return t()
                }
                var g = document.createElement("link");
                g.rel = "stylesheet",
                    g.type = "text/css",
                    g.onload = t,
                    g.onerror = function (t) {
                        var r = t && t.target && t.target.src || a
                            , i = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                        i.request = r,
                            delete n[e],
                            g.parentNode.removeChild(g),
                            o(i)
                    }
                    ,
                    g.href = a,
                    document.getElementsByTagName("head")[0].appendChild(g)
            }
        )).then((function () {
                n[e] = 0
            }
        )));
        var o = a[e];
        if (0 !== o)
            if (o)
                t.push(o[2]);
            else {
                var r = new Promise((function (t, r) {
                        o = a[e] = [t, r]
                    }
                ));
                t.push(o[2] = r);
                var i, u = document.getElementsByTagName("head")[0], c = document.createElement("script");
                c.charset = "utf-8",
                    c.timeout = 120,
                l.nc && c.setAttribute("nonce", l.nc),
                    c.src = function (e) {
                        return l.p + "js/" + ({
                            1: "vendors~csgoLive~dota2Live~index~league~leagueLol~leaugeVa~lolLive",
                            2: "vendors~csgoLive~dota2Live~index~lolLive~owlive~pubglive",
                            3: "vendors~LeagueCsgo~dota2Live~index~league~lolLive",
                            4: "LeagueCsgo~leaugeVa",
                            5: "csgoLive~owlive~pubglive",
                            6: "leaugeVa",
                            7: "LeagueCsgo",
                            9: "csgoLive",
                            10: "dota2Live",
                            11: "index",
                            12: "league",
                            13: "leagueLol",
                            14: "lolLive",
                            15: "match10",
                            16: "notfound",
                            17: "owlive",
                            18: "pubglive"
                        }[e] || e) + "." + {
                            1: "1af4a7d8",
                            2: "5dc58ed8",
                            3: "294dc529",
                            4: "6a6cf018",
                            5: "3019c0c9",
                            6: "f3470178",
                            7: "364e5fa7",
                            9: "8120897f",
                            10: "2c284bde",
                            11: "f6ec2522",
                            12: "e777e6bd",
                            13: "a157b060",
                            14: "09079c02",
                            15: "b35fd6f2",
                            16: "dae3957f",
                            17: "a4cc97fb",
                            18: "804b5e49"
                        }[e] + ".js"
                    }(e),
                    i = function (t) {
                        c.onerror = c.onload = null,
                            clearTimeout(s);
                        var o = a[e];
                        if (0 !== o) {
                            if (o) {
                                var r = t && ("load" === t.type ? "missing" : t.type)
                                    , n = t && t.target && t.target.src
                                    , i = new Error("Loading chunk " + e + " failed.\n(" + r + ": " + n + ")");
                                i.type = r,
                                    i.request = n,
                                    o[1](i)
                            }
                            a[e] = void 0
                        }
                    }
                ;
                var s = setTimeout((function () {
                        i({
                            type: "timeout",
                            target: c
                        })
                    }
                ), 12e4);
                c.onerror = c.onload = i,
                    u.appendChild(c)
            }
        return Promise.all(t)
    }
        ,
        l.m = e,
        l.c = r,
        l.d = function (e, t, o) {
            l.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: o
            })
        }
        ,
        l.r = function (e) {
            "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(e, "__esModule", {
                    value: !0
                })
        }
        ,
        l.t = function (e, t) {
            if (1 & t && (e = l(e)),
            8 & t)
                return e;
            if (4 & t && "object" === typeof e && e && e.__esModule)
                return e;
            var o = Object.create(null);
            if (l.r(o),
                Object.defineProperty(o, "default", {
                    enumerable: !0,
                    value: e
                }),
            2 & t && "string" != typeof e)
                for (var r in e)
                    l.d(o, r, function (t) {
                        return e[t]
                    }
                        .bind(null, r));
            return o
        }
        ,
        l.n = function (e) {
            var t = e && e.__esModule ? function () {
                    return e.default
                }
                : function () {
                    return e
                }
            ;
            return l.d(t, "a", t),
                t
        }
        ,

        l.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        l.p = "https://static.vpgame.com/schedule/3.5.5/",
        l.oe = function (e) {
            throw console.error(e),
                e
        }
    ;
    var u = window.__LOADABLE_LOADED_CHUNKS__ = window.__LOADABLE_LOADED_CHUNKS__ || []
        , c = u.push.bind(u);
    u.push = t,
        u = u.slice();
    for (var s = 0; s < u.length; s++)
        t(u[s]);
    var d = c;

    var vgg = l('aCH8');
    window.vga = l.n(vgg)
}([]);


l = function (e) {
    return u()(parseInt(2 * e / 3 + 4 - 5))
};

var c = Date.now()
    , u = l(c);