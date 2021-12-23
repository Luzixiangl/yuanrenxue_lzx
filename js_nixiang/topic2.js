// 缺啥补啥

function SDK_2() {
    window = this;

    // md5.js
    var hexcase = 0;
    var chrsz = 8;

    function bit_rol(num, cnt) {
        return (num << cnt) | (num >>> (32 - cnt));
    }

    function safe_add(x, y) {
        var lsw = (x & 0xFFFF) + (y & 0xFFFF);
        var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
        return (msw << 16) | (lsw & 0xFFFF);
    }

    function md5_cmn(q, a, b, x, s, t) {
        return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b);
    }

    function md5_ff(a, b, c, d, x, s, t) {
        return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);
    }

    function md5_gg(a, b, c, d, x, s, t) {
        return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);
    }

    function md5_hh(a, b, c, d, x, s, t) {
        return md5_cmn(b ^ c ^ d, a, b, x, s, t);
    }

    function md5_ii(a, b, c, d, x, s, t) {
        return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);
    }

    function core_md5(x, len) {
        /* append padding */
        x[len >> 5] |= 0x80 << ((len) % 32);
        x[(((len + 64) >>> 9) << 4) + 14] = len;

        var a = 1732584193;
        var b = -271733879;
        var c = -1732584194;
        var d = 271733878;

        for (var i = 0; i < x.length; i += 16) {
            var olda = a;
            var oldb = b;
            var oldc = c;
            var oldd = d;

            a = md5_ff(a, b, c, d, x[i + 0], 7, -680876936);
            d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
            c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
            b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
            a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
            d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
            c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
            b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
            a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
            d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
            c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
            b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
            a = md5_ff(a, b, c, d, x[i + 12], 7, 1804603682);
            d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
            c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
            b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);

            a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
            d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
            c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
            b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
            a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
            d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
            c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
            b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
            a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
            d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
            c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
            b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
            a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
            d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
            c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
            b = md5_gg(b, c, d, a, x[i + 12], 20, -1926607734);

            a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
            d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
            c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
            b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
            a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
            d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
            c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
            b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
            a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
            d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
            c = md5_hh(c, d, a, b, x[i + 3], 16, -722521979);
            b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
            a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
            d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
            c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
            b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);

            a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
            d = md5_ii(d, a, b, c, x[i + 7], 10, 1126891415);
            c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
            b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
            a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
            d = md5_ii(d, a, b, c, x[i + 3], 10, -1894986606);
            c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
            b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
            a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
            d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
            c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
            b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
            a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
            d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
            c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
            b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);

            a = safe_add(a, olda);
            b = safe_add(b, oldb);
            c = safe_add(c, oldc);
            d = safe_add(d, oldd);
        }
        return Array(a, b, c, d);

    }

    function binl2hex(binarray) {
        var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var str = "";
        for (var i = 0; i < binarray.length * 4; i++) {
            str += hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8 + 4)) & 0xF) +
                hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8)) & 0xF);
        }
        return str;
    }

    function str2binl(str) {
        var bin = Array();
        var mask = (1 << chrsz) - 1;
        for (var i = 0; i < str.length * chrsz; i += chrsz)
            bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << (i % 32);
        return bin;
    }

    function hex_md5(s) {
        return binl2hex(core_md5(str2binl(s), s.length * chrsz));
    }


    var _$oa = ['d2hpbGUgKHRydWUpIHt9', 'VWdMVHI=', 'RXh1TGk=', 'dmFsdWVPZg==', 'cnlSeXU=', 'QlRhVFM=', 'YlNVVHA=', 'RnhpS1g=', 'YXBwbHk=', 'enBDZVA=', 'T2hhb3U=', 'WHBPd1U=', 'cmVsb2Fk', 'T1h3QnA=', 'elVDRXY=', 'TEhRQkY=', 'ZnVuY3Rpb24gKlwoICpcKQ==', 'TFpOU0Q=', 'RXhQT2Y=', 'aVNDbEk=', 'Z2tmcGU=', 'bGVuZ3Ro', 'YnRvYQ==', 'dnVZR0I=', 'YUdJZ2U=', 'RkRKREo=', 'c3RyaW5n', 'Y2hhaW4=', 'Wk5PWVY=', 'bG9n', 'YXRWc3I=', 'blRrcU4=', 'V1RzUmE=', 'TE1NQ24=', 'XCtcKyAqKD86W2EtekEtWl8kXVswLTlhLXpBLVpfJF0qKQ==', 'VEVOR3Y=', 'c3NORVo=', 'c1lrdUk=', 'RVl2WGc=', 'RFZpY00=', 'UVBWT1Q=', 'aW95VnU=', 'Ympva2I=', 'TUNHWWI=', 'ZGR1aEo=', 'VFdJaUQ=', 'ZVF4bEk=', 'RkpTVlg=', 'WGRnWU4=', 'ZXFUUHM=', 'YVBacHo=', 'YmxUeHA=', 'WGNSQ3c=', 'ZXdYQm8=', 'VURkaFY=', 'SERDYks=', 'RURPcno=', 'eXdEZUM=', 'RlBzUHY=', 'RFh5WUo=', 'TmtWdVM=', 'c2lnbj0=', 'c0FyWHc=', 'Y29va2ll', 'TU52cFY=', 'Z1lJRG0=', 'VU1mSHk=', 'ZU92R0g=', 'c3RhdGVPYmplY3Q=', 'dGVzdA==', 'V09tTWk=', 'RlljRXk=', 'eFVwS2Q=', '5q2k572R6aG15Y+X44CQ54ix6ZSt5LqR55u+IFYxLjAg5Yqo5oCB54mI44CR5L+d5oqk', 'YWlkaW5nX3dpbg==', 'bml6c0Q=', 'a3dEVWQ=', 'TEhoa2M=', 'bFhEVU8=', 'alpISWI=', 'Wm94YmI=', 'SGlTaFE=', 'dkhaek4=', 'cm91bmQ=', 'dnBNeFE=', 'Z2FSblY=', 'dXRlT3M=', 'Y2FsbA==', 'V3lPa04=', 'RHRISGk=', 'YVFBclM=', 'Y29uc3RydWN0b3I=', 'aUJtZHI=', 'cEtyb1g=', 'THlsaFU=', 'RUhsdVU=', 'em1yb00=', 'Q0JGTVQ=', 'bFdjenA=', 'Z0lJa0w=', 'b2t3Zmw=', 'TkVRcmQ=', 'aW5wdXQ=', 'cWRFaXI=', 'YkRVaGs=', 'TGpMTk8=', 'bUxkZ2Y='];
    (function (a, b) {
        var c = function (f) {
            while (--f) {
                a['push'](a['shift']());
            }
        };
        c(++b);
    }(_$oa, 0x197));

    var _$ob = function (a, b) {
        a = a - 0x0;
        var c = _$oa[a];
        if (_$ob['PQtOiV'] === undefined) {
            (function () {
                var f;
                try {
                    var h = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');');
                    f = h();
                } catch (i) {
                    f = window;
                }
                var g = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                f['atob'] || (f['atob'] = function (j) {
                        var k = String(j)['replace'](/=+$/, '');
                        var l = '';
                        for (var m = 0x0, n, o, p = 0x0; o = k['charAt'](p++); ~o && (n = m % 0x4 ? n * 0x40 + o : o,
                        m++ % 0x4) ? l += String['fromCharCode'](0xff & n >> (-0x2 * m & 0x6)) : 0x0) {
                            o = g['indexOf'](o);
                        }
                        return l;
                    }
                );
            }());
            _$ob['KJkKEk'] = function (e) {
                var f = atob(e);
                var g = [];
                for (var h = 0x0, j = f['length']; h < j; h++) {
                    g += '%' + ('00' + f['charCodeAt'](h)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(g);
            }
            ;
            _$ob['XklnxL'] = {};
            _$ob['PQtOiV'] = !![];
        }
        var d = _$ob['XklnxL'][a];
        if (d === undefined) {
            c = _$ob['KJkKEk'](c);
            _$ob['XklnxL'][a] = c;
        } else {
            c = d;
        }
        return c;
    };

    var a = {
        'CBFMT': _$ob('0x25'),
        'blTxp': _$ob('0x37'),
        'eOvGH': function (d, e) {
            return d(e);
        },
        'XcRCw': 'init',
        'gYIDm': function (d, e) {
            return d + e;
        },
        'iBmdr': _$ob('0x30'),
        'OXwBp': _$ob('0x10'),
        'MPnQl': function (d) {
            return d();
        },
        'HiShQ': function (d, e, f) {
            return d(e, f);
        },
        'RSzSa': function (d, e) {
            return d === e;
        },
        'vokqs': _$ob('0x57'),
        'MCGYb': _$ob('0xf'),
        'EYvXg': _$ob('0x15'),
        'TWIiD': 'counter',
        'ExuLi': function (d, e) {
            return d !== e;
        },
        'jZFev': _$ob('0x36'),
        'WyOkN': function (d, e) {
            return d(e);
        },
        'vHZzN': function (d, e) {
            return d + e;
        },
        'dduhJ': _$ob('0x5e'),
        'FPsPv': function (d, e) {
            return d + e;
        },
        'gkfpe': _$ob('0x5f'),
        'BTaTS': function (d, e) {
            return d(e);
        },
        'LHQBF': function (d, e) {
            return d + e;
        },
        'okwfl': function (d, e) {
            return d(e);
        },
        'aGIge': function (d, e) {
            return d / e;
        },
        'Zoxbb': function (d, e) {
            return d + e;
        },
        'FDKDK': function (d, e) {
            return d + e;
        },
        'SbEID': function (d, e) {
            return d + e;
        },
        'flplI': function (d, e) {
            return d + e;
        },
        'Ztnss': _$ob('0x52'),
        'lZnZY': ';\x20path=/'
    };

    var c = new Date()[_$ob('0x18')]();
    // var c = 1587102734000;   // 题目的时间戳
    window.btoa = require('btoa');
    token = window[_$ob('0x2b')](a[_$ob('0x4f')](a['gkfpe'], a[_$ob('0x2')](String, c)));
    md = a[_$ob('0x1a')](hex_md5, window[_$ob('0x2b')](a[_$ob('0x24')](a[_$ob('0x29')], a[_$ob('0xe')](String, Math[_$ob('0x68')](a[_$ob('0x2d')](c, 0x3e8))))));

    var cookie = a[_$ob('0x24')](a[_$ob('0x65')](a['FDKDK'](a['SbEID'](a['SbEID'](a['flplI'](a['Ztnss'], Math[_$ob('0x68')](a[_$ob('0x2d')](c, 0x3e8))), '~'), token), '|'), md), a['lZnZY']);
    return cookie
}

console.log(SDK_2());