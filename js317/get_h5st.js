const CryptoJS = require('crypto-js');
const md5 = require('md5');
// 引入自定义的 mathOperations 模块
const __genDefaultKey = require('./__genDefaultKey.js');
// 引入自定义的 mathOperations 模块
const _defaultToken = require('./_defaultToken.js');
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

// token 会变
const params = {
    "floorToken": "9a784b4c-0124-4e73-957d-12493d77e201",
    "dataSourceCode": "signIn",
    "argMap": {
        "currSignCursor": 6,
        "signActId": 583
    },
    "riskInformation": {}
}
const functionId = 'pg_interact_interface_invoke'
const appid = 'jd-bean-task'
const signAppId = 'a7c04'
const data = {
    functionId,
    appid,
    signAppId,//非必传，自定义加固appid
    body: JSON.stringify(params),
}
console.info("data",data)
// 将对象转换为数组，每个元素为[key, value]形式
const items = Object.entries(data);

// 对数组进行排序，这里以字母顺序排序为例
items.sort((a, b) => a[0].localeCompare(b[0]));

// 将排序后的数组转换回对象
const bParams = Object.fromEntries(items);

console.info('bParams', bParams);
const requiredParamList = ['functionId', 'appid', 'client', 'body', 'clientVersion', 'sign', 't', 'jsonp']
const paramsSign = requiredParamList.reduce((acc, curr) => {
    let value = bParams[curr]
    if ((value)) {
        if (curr === 'body') {
            value = typeof value === 'string' ? sha256(value).toString() : sha256(JSON.stringify(value)).toString()
        }
        acc[curr] = value
    }
    return acc
}, {})


console.info('paramsSign', paramsSign);
// 先获取对象的所有键，并按字母顺序排序
const sortedKeys = Object.keys(paramsSign).sort();
// 然后使用map()方法按排序后的键生成新的对象数组
const t = sortedKeys.map(key => ({'key': String(key), 'value': paramsSign[key]}));
console.info("t", t)


function __genKey(tk, fp, ts, ai, algo) {
  var rd='4PmbC8rN14ep';var str="".concat(tk).concat(fp).concat(ts).concat(ai).concat(rd);return algo.MD5(str);
}

// const i = Date.now()
const i = 1713237817061
const a = format(i, 'yyyyMMddhhmmssSSS');
const u = a.concat('88')
console.info("i", i, "a", a, 'u', u)

const _fingerprint = 'ziigty5md0ctcch1'
const _appId = signAppId

const aes_iv = '0102030405060708'
const aes_key = 'r1T.6Vinpb.k+/a)'
const env = {
    "sua": "Windows NT 10.0; Win64; x64",
    "pp": {
        "p1": "jd_4536d74677e8d"
    },
    "extend": {
        "wd": 0,
        "l": 0,
        "ls": 5,
        "wk": 0,
        "bu1": "0.1.7",
        "bu2": -1,
        "bu3": 20,
        "bu4": 0,
        "bu5": 0
    },
    "random": "KVJ6JEdcxR6g",
    "v": "h5_file_v4.4.0",
    "fp": _fingerprint
}
function collect() {

    let iv = CryptoJS.enc.Utf8.parse(aes_iv), key = CryptoJS.enc.Utf8.parse(aes_key),
        data = CryptoJS.enc.Utf8.parse(JSON.stringify(env, null, 2));  // data
    aes = CryptoJS.AES.encrypt(data, key, {
        iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7
    });
    return aes.ciphertext.toString()//aes.toString()

}

const e = collect();
console.info("e",e)

const defaultToken = 'tk02wcc2e1d2141lMSszeDIrM3lz_oIsNUArUsMGZ0a5l0V_sCorwFZXUZKQGWfZaKLhgU7Gnfj8VWrlUeNyX4uPaheI'
// const defaultToken = _defaultToken.genLocalTK(_fingerprint)

const o = __genDefaultKey.__genDefaultKey(defaultToken, _fingerprint, u, signAppId);

console.info("o", o)

function __genSign(e, t) {
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

const s = __genSign(o, t)
console.info("s", s)

function __genSignParams(t, e, r, n) {
    return ["" + r, "" + _fingerprint, "" + _appId, "" + defaultToken, "" + t, "" + "4.4", "" + e, "" + n].join(";")
}

const h = __genSignParams(s, i, a, e);
console.info("h",h)
