const CryptoJS = require("crypto-js");

function J(t, e) {
    var r = [
        "x19HBgDVCML0Ag0",
        "x19Yzxf1zxn0rgvWCYb1C2uGBMv3igzWlcbMCdO",
        "mtC2nLbfr3PhDG",
        "lcbZAwDUzwrtDhi6",
        "CMv0DxjUia",
        "yNLUvu0",
        "yNv5wue",
        "BdfMBa",
        "BwfPBI5ZAwDUi19FCMvXDwvZDerLChm",
        "Dw5RBM93BIbLCNjVCG",
        "mJyZA2njCxj0",
        "CJfulJzwAw5WyI5RkY9Hkq",
        "x19Yzxf1zxn0rgvWCW",
        "ExL5Eu1nzgrOAg1TC3ntu1m",
        "mtyXmZKYn3fHs1DpDG",
        "zxH0zw5K",
        "Dg9Rzw4GAxmGzw1WDhK",
        "x19Yzxf1zxn0rgvWCYbLBMqU",
        "wMPQBve",
        "Bg9JywXFA2v5xZm",
        "z2v0vg9Rzw4",
        "x19Yzxf1zxn0qwXNB3jPDgHTt25Jzq",
        "ohjxvfP0AW",
        "x19WyxjZzufSz29YAxrOBq",
        "su5vrgK",
        "rK5gtgK",
        "mtKZmdKWAxLXALfP",
        "mJaXnJGYz29tEe1P",
        "AgLrugO",
        "lgv4ChjLC3m9",
        "x19JB2XSzwn0igvUDKnVBgXLy3q9",
        "CgfYyw1ZigLZig5VDcbHihbSywLUig9IAMvJDa",
        "CYnS",
        "Cu9eELG",
        "CvyHk0eH",
        "CgfYyw1ZigLZigvTChr5igfMDgvYigv4y2X1zgLUzYaIDw5ZywzLiIbWyxjHBxm",
        "CeTLsvG",
        "ihrVA2vUoG",
        "yNuY",
        "CgfYyw1ZigLZigvTChr5",
        "nc40",
        "Chv4zM4",
        "tw9rtvC",
        "x19JAgvJA1bHCMfTCW",
        "qwrnDhG",
        "x19Nzw5ezwzHDwX0s2v5igLUChv0pq",
        "y3jLyxrLigLUC3rHBMnLihDPDgGGyxbWswq9",
        "x19PBMLdB25MAwC",
        "nda2EM56Bujj",
        "x19Yzxf1zxn0qwXNB3jPDgHTigvUDKnVBgXLy3q9",
        "v2jxthm",
        "C0Tmwwu",
        "x19Yzxf1zxn0qwXNB3jPDgHT",
        "DxnLig5VCM1HBfrVA2vU",
        "x19Nzw5tAwDU",
        "CLbUANy",
        "x19Yzxf1zxn0rgvWCYWGx19WyxjZzufSz29YAxrOBsbYzxn1Bhq6",
        "x19JB2XSzwn0",
        "lcbHBgDVoG",
        "mNWWFdn8nhWX",
        "x19Yzxf1zxn0rgvWCYbYzxf1zxn0ihrVA2vUigzHAwXLzcWGzxjYB3i6ia",
        "C2LNBIbLBgfWC2vKihrPBwuH",
        "CgfYyw1ZignVBNrHAw5ZihjLC2vYDMvKihbHCMfTig5HBwuU",
        "BwrQDM0",
        "BwfPBI5ZAwDUi19Fzgv0zwn0Aw5N",
        "mcfa",
        "x19Nzw5ezwzHDwX0s2v5",
        "mtbADw5Sz3i",
        "x19TywTLu2LNBIWGCMvZDwX0oG",
        "CwvuyNi",
        "ota3mtq5u01dq1Lr",
        "CxvLCNLtzwXLy3rVCG",
        "x19Yzxf1zxn0rgvWCYbZDgfYDc4",
        "x19Nzw5tAwDUlcbWyxjHBxntDhi6",
        "uvbpEfe",
        "z2vUzxjHDguGA2v5igzHAwXLza",
        "C2v0DgLUz3mUyxbWswqGBxvZDcbIzsbHig5VBI1LBxb0EsbZDhjPBMC",
        "EujKuMS",
        "tgfMvgO",
        "lcbJAgvJAYbZDg9YywDLigzWoG",
        "x19Yzxf1zxn0qwXNB3jPDgHTigvUzc4",
        "C3vJy2vZCW",
        "mtaYoti1mKTSBNPnza",
        "x19Nzw5tAwDUugfYyw1Z",
        "zxfIAve",
        "mJuYDxr0rxHy",
        "nezoAxzXAq",
        "x19WyxjZzvrVA2vU",
        "C2LNBG",
        "x19Yzxf1zxn0qwXNB3jPDgHTihjLCxvLC3qGC3vJy2vZCYeSignOzwnRig1LBw9YEsbMCdO",
        "lcb0B2TLBJO",
        "lgTLEt0",
        "DgvZDcbLCNi",
        "lcbMCdO",
        "lcbZDg9YywDLrNa6",
        "x19Yzxf1zxn0qwXNB3jPDgHTihn0yxj0lG",
        "x19Yzxf1zxn0rgvWCYb1C2uGy2fJAguGzNaSigzWoG",
        "otqWotrgt2vdDKe",
        "mtuZsvfzBfn0",
        "x19TywTLu2LNBG"
    ];
    return J = function (e, n) {
        var o = r[e -= 424];
        if (void 0 === J.NWhDYN) {
            J.KnAaeJ = function (t) {
                for (var e, r, n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=", o = "", i = "", a = 0, u = 0; r = t.charAt(u++); ~r && (e = a % 4 ? 64 * e + r : r,
                a++ % 4) ? o += String.fromCharCode(255 & e >> (-2 * a & 6)) : 0)
                    // r = (0,
                    //  v.default)(n).call(n, r);
                    r = n.indexOf(r);
                for (var c = 0, s = o.length; c < s; c++) {
                    // var f;
                    // i += "%" + (0,
                    // d.default)(f = "00" + o.charCodeAt(c).toString(16)).call(f, -2)
                    var f = "00" + o.charCodeAt(c).toString(16)
                    i += '%' + f.slice(-2)
                }
                return decodeURIComponent(i)
            }
                ,
                t = arguments,
                J.NWhDYN = !0
        }
        var i = e + r[0].substring(0, 2)
            , a = t[i];
        return a ? o = a : (o = J.KnAaeJ(o),
            t[i] = o),
            o
    }
        ,
        J(t, e)
}

const algos = {
    HmacMD5: function (text, secret) {
        return CryptoJS.HmacMD5(text, secret)
    },
    HmacSHA256: function (text, secret) {
        return CryptoJS.HmacSHA256(text, secret)
    },
    HmacSHA512: function (text, secret) {
        return CryptoJS.HmacSHA512(text, secret)
    },
    MD5: function (text) {
        return CryptoJS.MD5(text)
    },
    SHA256: function (text) {
        return CryptoJS.SHA256(text)
    },
    SHA512: function (text) {
        return CryptoJS.SHA512(text)
    },
}
function init(t, e) {
    t = this.words = t || [],
        this.sigBytes = e
}

function n(t, r, n) {
    for (var o = [], i = 0, a = 0; a < r; a++)
        if (a % 4) {
            var u = n[t.charCodeAt(a - 1)] << a % 4 * 2 | n[t.charCodeAt(a)] >>> 6 - a % 4 * 2;
            o[i >>> 2] |= u << 24 - i % 4 * 8,
                i++
        }
    return new init(o, i)
}

let Base64 = {
    stringify: function (t) {
        var e = t.words
            , r = t.sigBytes
            , n = this._map;
        t.clamp();
        for (var o = [], i = 0; i < r; i += 3)
            for (var a = (e[i >>> 2] >>> 24 - i % 4 * 8 & 255) << 16 | (e[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255) << 8 | e[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, u = 0; u < 4 && i + .75 * u < r; u++)
                o.push(n.charAt(a >>> 6 * (3 - u) & 63));
        var c = n.charAt(64);
        if (c)
            for (; o.length % 4;)
                o.push(c);
        return o.join("")
    },
    parse: function (t) {
        var e = t.length
            , r = this._map
            , o = this._reverseMap;
        if (!o) {
            o = this._reverseMap = [];
            for (var i = 0; i < r.length; i++)
                o[r.charCodeAt(i)] = i
        }
        var a = r.charAt(64);
        if (a) {
            var u = t.indexOf(a);
            -1 !== u && (e = u)
        }
        return n(t, e, o)
    },
    _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
}

function toBase64(t) {
    return (t).replace(/-/g, "+").replace(/_/g, "/")
}

function hstringify(t) {
    for (var e = t.words, r = t.sigBytes, n = [], o = 0; o < r; o++) {
        var i = e[o >>> 2] >>> 24 - o % 4 * 8 & 255;
        n.push(String.fromCharCode(i))
    }
    return n.join("")
}

let t = 'tk02wae1f1c4241lMngzKzIrMnFHfz26cY7cWcC60ZE0jzlBEL6FZvx44_ZxVz4Ysx35WrVikWFGaMUyRHotFnAdIARN'
console.info(decodeURIComponent(escape(hstringify(Base64.parse(toBase64(t.substring(16, 28)))))))


function __genDefaultKey(t, e, r, n) {
    var o = this
        o.__algorithm = function (f,r,t){
           return  f(r,t).toString()
        }
        , i = J
        , a = {
            XVTOq: function (t, e) {
                return t(e)
            },
            OSlAp: function (t, e) {
                return t(e)
            },
            WSKsI: function (t, e, r) {
                return t(e, r)
            },
            MaaZO: i(477),
            NhVvm: function (t, e) {
                return t !== e
            },
            aWUBR: i(508),
            vLEvy: function (t, e) {
                return t + e
            },
            iIdYQ: i(469),
            rYEWn: i(453)
        }
        , u = ""
        , c = i(458)
        , s = "" + t + e + r + n + c
        // , f = B.default.stringify(M.default.parse((0,
        // U.toBase64)(this.__parseToken(t, 16, 28))))
        , f = decodeURIComponent(escape(hstringify(Base64.parse(toBase64(t.substring(16, 28))))))
        , l = f.match(/^[123]([x+][123])+/);
    if (l) {
        var h = l[0].split("")
            ,  p = {
    local_key_1: algos.MD5,
    local_key_2: algos.SHA256,
    local_key_3: algos.HmacSHA256,}
            , d = "";


          h.forEach((e) => {
              var r, n = i;
                if (isNaN(e)){
                    r = ["+", "x"]
                    r.indexOf(e)>= 0 && (d = e);
                }else if (a.NhVvm(n(452), n(452))) {
                    var f = d
                        , l = f.appId
                        , h = f.debug
                        , g = f.onSign
                        , y = f.onRequestToken
                        , m = f.onRequestTokenRemotely;
                    !(a.XVTOq(e, _$o.appId) && l.appId) && _$K.error(n(500)),
                        o._appId = l || "",
                    o._appId && (o._storagetokenKey = o._storagetokenKey + "_" + o._appId + "_" + o._version,
                        o._storageAlgnKey = o._storageAlgnKey + "_" + o._appId + "_" + o._version,
                        o._storageFpKey = o._storageFpKey + "_" + o._appId + "_" + o._version),
                        o._debug = g(h),
                        o._onSign = y(g) ? g : m,
                        o._onRequestToken = _$k(y) ? y : _$O,
                        o._onRequestTokenRemotely = a.OSlAp(_$u, m) ? m : _$L,
                        a.WSKsI(_$D, o._debug, n(470) + o._appId),
                        o._onRequestToken({
                            code: 0,
                            message: a.MaaZO
                        }),
                        o._onRequestTokenRemotely({
                            code: 200,
                            message: ""
                        })
                } else {
                    var w = "" + 'local_key_' + e;
                    if (p[w]) {
                        if (!a.NhVvm(a.aWUBR, n(474))) {
                            if (c && s) {
                                o._token = p || "",
                                    o.__genKey = d && new e(n(428) + _$o)() || null;
                                var _ = !(!o._token || !o.__genKey);
                                return o._isNormal = _,
                                    _
                            }
                            return !1
                        }
                        switch (d) {
                            case "+":
                                u = "" + u + o.__algorithm(p[w], s, t);
                                break;
                            case "x":
                                u = o.__algorithm(p[w], u, t);
                                break;
                            default:
                                u = o.__algorithm(p[w], s, t)
                        }
                    }
                }
          });



        // (0,
        //     y.default)(h).call(h, (function (e) {
        //         var r, n = i;
        //         if (isNaN(e))
        //             (0,
        //                 v.default)(r = ["+", "x"]).call(r, e) >= 0 && (d = e);
        //         else if (a.NhVvm(n(452), n(452))) {
        //             var f = d
        //                 , l = f.appId
        //                 , h = f.debug
        //                 , g = f.onSign
        //                 , y = f.onRequestToken
        //                 , m = f.onRequestTokenRemotely;
        //             !(a.XVTOq(e, _$o.appId) && l.appId) && _$K.error(n(500)),
        //                 o._appId = l || "",
        //             o._appId && (o._storagetokenKey = o._storagetokenKey + "_" + o._appId + "_" + o._version,
        //                 o._storageAlgnKey = o._storageAlgnKey + "_" + o._appId + "_" + o._version,
        //                 o._storageFpKey = o._storageFpKey + "_" + o._appId + "_" + o._version),
        //                 o._debug = g(h),
        //                 o._onSign = y(g) ? g : m,
        //                 o._onRequestToken = _$k(y) ? y : _$O,
        //                 o._onRequestTokenRemotely = a.OSlAp(_$u, m) ? m : _$L,
        //                 a.WSKsI(_$D, o._debug, n(470) + o._appId),
        //                 o._onRequestToken({
        //                     code: 0,
        //                     message: a.MaaZO
        //                 }),
        //                 o._onRequestTokenRemotely({
        //                     code: 200,
        //                     message: ""
        //                 })
        //         } else {
        //             var w = "" + O.LOCAL_ALGORITHM_PREFIX + e;
        //             if (p[w]) {
        //                 if (!a.NhVvm(a.aWUBR, n(474))) {
        //                     if (c && s) {
        //                         o._token = p || "",
        //                             o.__genKey = d && new e(n(428) + _$o)() || null;
        //                         var _ = !(!o._token || !o.__genKey);
        //                         return o._isNormal = _,
        //                             _
        //                     }
        //                     return !1
        //                 }
        //                 switch (d) {
        //                     case "+":
        //                         u = "" + u + o.__algorithm(w, s, t);
        //                         break;
        //                     case "x":
        //                         u = o.__algorithm(w, u, t);
        //                         break;
        //                     default:
        //                         u = o.__algorithm(w, s, t)
        //                 }
        //             }
        //         }
        //     }
        // ))
    }
    return  u
}

let _defaultToken = 'tk02w8de81bb941lMXgxKzN4M2M4LZDOeSOk6yfKbUSVQ3Nr5DQSApncBYKM398zlIYKgokdYgsu5lIUaw2yI63nHTVK'
let _fingerprint = 'ziigty5md0ctcch1'
let u = '2024041609102637488'
let _appId = 'a7c04'

// console.info("__genDefaultKey", __genDefaultKey(_defaultToken, _fingerprint, u, _appId))

module.exports = {
    __genDefaultKey,
};