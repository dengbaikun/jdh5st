const CryptoJS = require("crypto-js");

function getRandomIDPro() {
    var t, e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}, r = e.size,
        n = void 0 === r ? 10 : r, o = e.dictType, i = void 0 === o ? "number" : o, a = e.customDict, u = "";
    if (a && "string" == typeof a)
        t = a;
    else
        switch (i) {
            case "alphabet":
                t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
                break;
            case "max":
                t = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-";
                break;
            default:
                t = "0123456789"
        }
    for (; n--;)
        u += t[Math.random() * t.length | 0];
    return u
}
 function pdefaultstr(t, e) {
    var r = 1
        , n = 0
        , o = t.length
        , i = 0
        , a = 0
        , u = 0;
    "number" == typeof e && (r = 65535 & e,
        n = e >>> 16);
    for (var c = 0; c < o;) {
        for (i = Math.min(o - c, 3850); i > 0;)
            (a = t.charCodeAt(c++)) < 128 ? r += a : a < 2048 ? (n += r += 192 | a >> 6 & 31,
                --i,
                r += 128 | 63 & a) : a >= 55296 && a < 57344 ? (n += r += 240 | (a = 64 + (1023 & a)) >> 8 & 7,
                --i,
                n += r += 128 | a >> 2 & 63,
                --i,
                n += r += 128 | (u = 1023 & t.charCodeAt(c++)) >> 6 & 15 | (3 & a) << 4,
                --i,
                r += 128 | 63 & u) : (n += r += 224 | a >> 12 & 15,
                --i,
                n += r += 128 | a >> 6 & 63,
                --i,
                r += 128 | 63 & a),
                n += r,
                --i;
        r = 15 * (r >>> 16) + (65535 & r),
            n = 15 * (n >>> 16) + (65535 & n)
    }
    return n % 65521 << 16 | r % 65521
}

function y(t) {
    var e = d
        , r = pdefaultstr(t);
    r = function (t, e) {
        return t >>> e
    }(r, 0);
    var n = e(265) + r.toString(16);
    return n.substr(n.length - 8)
}

function m(t, e) {
    var r = [
        "nJi1tfDgCg96",
        "mJKZodK0oen1EhfcrG",
        "nJGWnZCWnePQt0ffBW",
        "m1zdELDnBq",
        "vLfYwLG",
        "ntu0nZqYowHqyNjjBq",
        "r3Pkz1G",
        "mZm0mteZnxf6s2D4Dq",
        "sgLpodeTrwK4ouri",
        "nJaXmfrHuuz5wG",
        "mdaWmdaWmda",
        "mJzrAvLqqLe",
        "nJq1nJD2zgjbwvO",
        "zuHmnhXgvYndAgmZi3e/ma",
        "Bwf4",
        "odC2mfjKtxz1uW",
        "mZi4ndziExv2yxG",
        "C1vJv1C",
        "sKPmBxu"
    ];
    return m = function (e, n) {
        var a = r[e -= 255];
        if (void 0 === m.nGopkV) {
            m.dYNTtF = function (t) {
                for (var e, r, n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=", a = "", u = "", c = 0, s = 0; r = t.charAt(s++); ~r && (e = c % 4 ? 64 * e + r : r,
                c++ % 4) ? a += String.fromCharCode(255 & e >> (-2 * c & 6)) : 0)
                    r = n.indexOf(r);
                for (var f = 0, l = a.length; f < l; f++) {
                    var h = "00" + a.charCodeAt(f).toString(16);
                    u += "%" + h.slice(-2)
                }
                return decodeURIComponent(u)
            }
                ,
                t = arguments,
                m.nGopkV = !0
        }
        var u = e + r[0].substring(0, 2)
            , c = t[u];
        return c ? a = c : (a = m.dYNTtF(a),
            t[u] = a),
            a
    }
        ,
        m(t, e)
}

var d = m;
buf = function (t, e) {
    var r = 1
        , n = 0
        , o = t.length
        , i = 0;
    "number" == typeof e && (r = 65535 & e,
        n = e >>> 16 & 65535);
    for (var a = 0; a < o;) {
        for (i = Math.min(o - a, 3850) + a; a < i; a++)
            n += r += 255 & t[a];
        r = 15 * (r >>> 16) + (65535 & r),
            n = 15 * (n >>> 16) + (65535 & n)
    }
    return n % 65521 << 16 | r % 65521
}

function x(t) {
    var e, r = d, n = function (t, e) {
            return t - e
        }, o = function (t, e) {
            return t !== e
        }, i = (e = new ArrayBuffer(2),
            new DataView(e).setInt16(0, 256, !0),
        256 === new Int16Array(e)[0]), a = Math.floor(t / Math.pow(2, 32)), u = t % Math.pow(2, 32), c = new ArrayBuffer(8),
        s = new DataView(c);
    return i ? o(r(273), r(261)) ? (s.setUint32(0, u, i),
        s.setUint32(4, a, i)) : (_$r += _$D[_$I.floor(3 * _$w.random())],
    _$L < n(_$k, 1) && (_$Z += _$C[_$j.floor(2 * _$h.random())])) : (s.setUint32(0, a, i),
        s.setUint32(4, u, i)),
        new Uint8Array(c)
}

od = function (t) {
    var e = t.forEach;
    return e
}

function w(t) {
    // return (0,
    //     u.default)(Array.prototype).call(t, (function (t) {
    //         var e;
    //         return (0,
    //             i.default)(e = "00" + (255 & t).toString(16)).call(e, -2)
    //     }
    // )).join("")

    let newArray = [t.length]


    Array.from(t).forEach((_, index) => {
        var e = "00" + (255 & _).toString(16);
        newArray[index] = e.slice(-2)
    });
    return newArray.join("")
}

function _(t) {
    var e = new Uint8Array(t.length);
    // Array.from(e).forEach((_, index) => {
    //        e[index] = t.charCodeAt(index);
    //    });
    return od(Array.prototype).call(e, (function (e, r, n) {
            var o = m;
            o(272) === o(259) ? r[n] = _$O.charCodeAt(_$U) : n[r] = t.charCodeAt(r)
        }
    )),
        function (t, e) {
            return t(e)
        }(w, e)
}

function init(t, e) {
    t = this.words = t || [],
        this.sigBytes = e
}

function sdefaultparse(t) {
    for (var e = t.length, r = [], n = 0; n < e; n += 2)
        r[n >>> 3] |= parseInt(t.substr(n, 2), 16) << 24 - n % 8 * 4;
    return new init(r, e / 2)
}

function ldefaultparse(t) {
    t = unescape(encodeURIComponent(t))
    for (var e = t.length, r = [], n = 0; n < e; n++)
        r[n >>> 2] |= (255 & t.charCodeAt(n)) << 24 - n % 4 * 8;
    return new init(r, e)
}

function hdefaultstringify(t) {
    // 创建一个足够大的 Buffer 来存储所有字节
    const buffer = Buffer.alloc(t.sigBytes);
    // 将每个整数的四个字节写入到 Buffer 中
    t.words.forEach((word, index) => {
        buffer.writeInt32BE(word, index * 4);
    });
    // 将 Buffer 转换为 Base64
    return buffer.toString('base64').replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "")
}


function genLocalTK(t) {
    var e = {
        nQaMT: function (t, e) {
            return t(e)
        },
        oBHbX: function (t, e) {
            return t + e
        },
        FXqyy: function (t, e) {
            return t + e
        },
        mzuVX: function (t, e) {
            return t + e
        },
        IGSzZ: function (t, e) {
            return t + e
        },
        ksuoM: function (t, e) {
            return t + e
        },
        pDGre: function (t, e) {
            return t + e
        }
    }
        , r = {
        magic: "tk",
        version: "02",
        platform: "w",
        expires: "41",
        producer: "l"
    };
    return r.expr = function () {
        for (var t = m, e = {
            gNKwD: function (t, e) {
                return t < e
            },
            IEPPS: function (t, e) {
                return t < e
            },
            EpXBX: function (t, e) {
                return t - e
            }
        }, r = getRandomIDPro({
            size: 32,
            dictType: t(269),
            customDict: null
        }), n = ["1", "2", "3"], o = ["+", "x"], i = 2 + Math.floor(4 * Math.random()), a = "", u = 0; e.gNKwD(u, i); u++)
            a += n[Math.floor(3 * Math.random())],
            e.IEPPS(u, e.EpXBX(i, 1)) && (a += o[Math.floor(2 * Math.random())]);
        a.length < 9 && (a += r.substr(0, 9 - a.length));
        // 将字符串转换为Buffer对象
        const buffer = Buffer.from(a);

        // 将Buffer转换为Base64编码的字符串
        const base64String = buffer.toString('base64');
        return base64String.replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "")
        // var s = p.parse(a)
        //     , f = h.default.stringify(s);
        // return (0,
        //     c.fromBase64)(f)
    }(),
        r.cipher = function (t) {
            var e = d
                , r = {
                MYyeR: function (t, e) {
                    return t(e)
                }
            };
            r.MYyeR(getRandomIDPro, {
                size: 32,
                dictType: e(269),
                customDict: null
            });
            var o = ""
                , i = Date.now()
                , u = "(>"
                , y = e(263)
                , m = function (t, e, r, n) {
                var o = {
                    qAvoG: d(265)
                }
                    , i = new Uint8Array(16);
                // (0,
                //     a.default)(Array.prototype).call(i, (function (e, r, n) {
                //         n[r] = t.charCodeAt(r)
                //     }
                // ));
                // 将 Uint8Array 转换为数组，使用 forEach 进行操作
                Array.from(i).forEach((_, index) => {
                    i[index] = t.charCodeAt(index);
                });
                var u = x(e)
                    , c = new Uint8Array(2);
                // (0,
                //     a.default)(Array.prototype).call(c, (function (t, e, n) {
                //         n[e] = r.charCodeAt(e)
                //     }
                // ));
                Array.from(c).forEach((_, index) => {
                    c[index] = r.charCodeAt(index);
                });
                var s = new Uint8Array(12);
                // (0,
                //     a.default)(Array.prototype).call(s, (function (t, e, r) {
                //         r[e] = n.charCodeAt(e)
                //     }
                // ));
                Array.from(s).forEach((_, index) => {
                    s[index] = n.charCodeAt(index);
                });
                var f = new Uint8Array(38);
                f.set(c),
                    f.set(s, 2),
                    f.set(u, 14),
                    f.set(i, 22);
                var l = buf(f);
                l >>>= 0;
                var h = o.qAvoG + l.toString(16);
                return h.substr(h.length - 8)
            }(t, i, u, y);
            o += _(m),
                o += _(u),
                o += _(y),
                o += function (t) {
                    return w(x(t))
                }(i),
                o += _(t);
            const aes_iv = '0102030405060708'
            const aes_key = 'eHL4|FW#Chc3#q?0'
            let iv = ldefaultparse(aes_iv), key = ldefaultparse(aes_key),
                data = sdefaultparse(o);  // data
            console.info("iv", iv)
            console.info("key", key)
            console.info("data", data)
            let aes = CryptoJS.AES.encrypt(data, key, {
                iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7
            });
            let ciphertext = hdefaultstringify(aes.ciphertext)
            return ciphertext
        }(t),
        r.adler32 = e.nQaMT(y, e.oBHbX(e.FXqyy(e.mzuVX(e.IGSzZ(r.magic + r.version, r.platform), r.expires), r.producer), r.expr) + r.cipher),
    e.ksuoM(e.mzuVX(e.pDGre(r.magic, r.version), r.platform) + r.adler32 + r.expires, r.producer) + r.expr + r.cipher
}


console.info(genLocalTK('i6y65zgnq1tthdq0'))


module.exports = {
    genLocalTK,
};