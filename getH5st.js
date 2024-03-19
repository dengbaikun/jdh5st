const CryptoJS = require('crypto-js');
const crypto = require('crypto');
const md5 = require('md5');
const fingerPrint = 'ti9gg5yydcututj6'
const appId = 'fb5df'
const aes_iv = '0102030405060708'
const aes_key = 'r1T.6Vinpb.k+/a)'
const token = 'tk03wbfb71c2918nIBy3aai71myljtZfYvbYsfVqC3XZupFMpxT_iGd401W015HRPrOM4i0oTW_AyEOnJkdEI46VWEuq'
const version = '4.4';

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

const randomId = getRandomIDPro({
    size: 11,
    dictType: 'max',
    customDict: null
})
console.log("getRandomIDPro", randomId)

const env = {
    "sua": "Windows NT 10.0; Win64; x64",
    "pp": {
        "p2": "jd_4536d74677e8d"
    },
    "extend": {
        "wd": 0,
        "l": 0,
        "ls": 5,
        "wk": 0,
        "bu1": "0.1.9",
        "bu2": -1,
        "bu3": 91,
        "bu4": 0,
        "bu5": 0
    },
    "random": randomId,
    "v": "h5_file_v4.4.0",
    "fp": fingerPrint,
    "bu1": "0.1.8"
}


function collect() {

    let iv = CryptoJS.enc.Utf8.parse(aes_iv), key = CryptoJS.enc.Utf8.parse(aes_key),
        data = CryptoJS.enc.Utf8.parse(JSON.stringify(env, null, 2));  // data
    aes = CryptoJS.AES.encrypt(data, key, {
        iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7
    });
    return aes.ciphertext.toString()//aes.toString()

}

function format() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : Date.now,
        r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "yyyy-MM-dd", n = new Date(e), o = r, i = {
            "M+": n.getMonth() + 1,
            "d+": n.getDate(),
            "D+": n.getDate(),
            "h+": n.getHours(),
            "H+": n.getHours(),
            "m+": n.getMinutes(),
            "s+": n.getSeconds(),
            "w+": n.getDay(),
            "q+": Math.floor((n.getMonth() + 3) / 3),
            "S+": n.getMilliseconds()
        };
    return /(y+)/i.test(o) && (o = o.replace(RegExp.$1, "".concat(n.getFullYear()).substr(4 - RegExp.$1.length))),
        Object.keys(i).forEach(function (t) {
            if (new RegExp("(".concat(t, ")")).test(o)) {
                var e, r = "S+" === t ? "000" : "00";
                o = o.replace(RegExp.$1, 1 == RegExp.$1.length ? i[t] : e = "".concat(r).concat(i[t]).substr("".concat(i[t]).length))
            }
        }),
        o
}

function sha256(text) {
    return CryptoJS.SHA256(text).toString()
}

function hmac(algorithm, text, secret) {
    hmac = crypto.createHmac(algorithm, secret);

    // 添加数据
    hmac.update(text);

    // 生成 HMAC
    return hmac.digest('hex');
}

function genKey(token, fingerprint, u, appId) {
    var rd = '1omnRMcSOOOQ';
    var str = "".concat(token).concat(fingerprint).concat(u).concat(appId).concat(rd);
    // return hmac('md5', str, token)
    // return CryptoJS.HmacMD5(str,token).toString();
    return CryptoJS.SHA256(str,token).toString();
}
function gensign(e, t) {
    var result = "";
    for (var i = 0; i < t.length; i++) {
        result += t[i].key + ":" + t[i].value + "&";
    }
    // 删除最后一个多余的&
    result = result.slice(0, -1);
    result = e + result + e
    result = md5(result)
    return result;
}


function getH5st(l) {
    // 先获取对象的所有键，并按字母顺序排序
    const sortedKeys = Object.keys(l).sort();
// 然后使用map()方法按排序后的键生成新的对象数组
    const t = sortedKeys.map(key => ({'key': String(key), 'value': l[key]}));
    console.log("sortedArray", t)
    const timestamp = Date.now()
    const date_time = format(timestamp, 'yyyyMMddhhmmssSSS')
    const u = date_time + '88'
    const env_data = collect();
    console.log("u", u)
    const key = genKey(token, fingerPrint, u, appId)
    console.log("env_data", env_data);
    console.log("date_time", date_time);
    console.log("timestamp", timestamp);
    console.log("genKey", key);
    const sign = gensign(key, t);
    console.log("sign", sign)
    const h5st = ["" + date_time, "" + fingerPrint, "" + appId, "" + token, "" + sign, "" + version, "" + timestamp, "" + env_data].join(";");
    console.log('h5st', h5st)
    return h5st
}
const a = {
    "skuId": 100011293139,
    "cat": "652,828,842",
    "area": "19_1666_36267_36272",
    "shopId": "1000085868",
    "venderId": 1000085868,
    "paramJson": "{\"platform2\":\"100000000001\",\"specialAttrStr\":\"p0pp1pppppppp1ppppppppppppppp\",\"skuMarkStr\":\"00\"}",
    "num": 1,
    "bbTraffic": "",
    "canvasType": 1
}
const dt = 1710236575236
console.log("dt",dt)
const r = JSON.stringify(a)
const d = {
    appid: "pc-item-soa",
    functionId: "pc_detailpage_wareBusiness",
    client: "pc",
    clientVersion: "1.0.0",
    t: dt,
    body: r
}
const l = JSON.parse(JSON.stringify(d));
l.body = sha256(r)
console.log("l.body",l.body)

console.log(getH5st(l))