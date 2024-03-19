function v() {
    var t = ["mZyZnLDHD2LhBW", "rNLlAwe", "AfHAvK0", "mtr6zLPWwuS", "Dxfswhu", "mJjPvufXuuu", "mZm3ofvfzg51DG", "mJGZmtj3y1Dur3O", "mxvJDdzKmgPOCq", "mJeXmtu1mJnVy1LsA3i", "ntG0mtqXmfbPtMvbDq", "nZG3ody2AfrMyKrU", "nde2ntvPCvbnz1K", "ve5psKi", "mtaXnJaYr1jPBxLm", "C1rKDM0", "mtjPte5Wqvi", "mZG4ChPmB2Di"];
    return (v = function () {
        return t
    })()
}

function d(t, e) {
    var r = v();
    return d = function (e, n) {
        var o = r[e -= 327];
        if (void 0 === d.BLagUU) {
            d.VTDShA = function (t) {
                for (var e, r, n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=", o = "", i = "", a = 0, u = 0; r = t.charAt(u++); ~r && (e = a % 4 ? 64 * e + r : r, a++ % 4) ? o += String.fromCharCode(255 & e >> (-2 * a & 6)) : 0) r = n.indexOf(r);
                for (var f = 0, l = o.length; f < l; f++) {
                    var h;
                    i += "%" + (h = "00" + o.charCodeAt(f).toString(16)).slice(-2)
                }
                return decodeURIComponent(i)
            }
                , t = arguments, d.BLagUU = !0
        }
        var i = e + r[0].substring(0, 2), a = t[i];
        return a ? o = a : (o = d.VTDShA(o), t[i] = o), o
    }
        , d(t, e)
}

function h(t, u) {
    var c = String.prototype[Symbol.iterator];
    var l, h = !0, d = !1;
    return {
        s: function () {
            c = c.call(t)
        }, n: function () {
            var t = c.next();
            return h = t.done, t
        }, e: function (t) {
            for (var r = [96, 99, 13, 77, 56, 13, 53], n = [], o = 0; ;) switch (r[o++]) {
                case 13:
                    n.pop();
                    break;
                case 53:
                    return;
                case 56:
                    l = n[n.length - 1];
                    break;
                case 77:
                    n.push(t);
                    break;
                case 96:
                    n.push(!0);
                    break;
                case 99:
                    d = n[n.length - 1]
            }
        }, f: function () {
            try {
                h || null == c.return || c.return()
            } finally {
                if (d) throw l
            }
        }
    }
}

function y(t, e) {
    var r, n = d, o = function (t, e) {
        return t < e
    }, i = function (t, e) {
        return t == e
    }, a = function (t, e) {
        return t < e
    }, u = [], c = t.length, s = h(t);
    try {
        for (s.s(); !(r = s.n()).done;) {
            var f = r.value;
            if (o(Math.random() * c, e) && (u.push(f), i(--e, 0))) break;
            c--
        }
    } catch (t) {
        s.e(t)
    } finally {
        s.f()
    }
    for (var l = "", p = 0; a(p, u.length); p++) {
        if (n(331) === n(328)) return 10 * e.random() | 0;
        var v = Math.random() * (u.length - p) | 0;
        l += u[v], u[v] = u[u.length - p - 1]
    }
    return l
}

function g() {
    return 10 * Math.random() | 0
}

function _(t, e) {
    for (var r = 0; r < e.length; r++) {
        -1 !== (t).indexOf(e[r]) && (t = t.replace(e[r], ""))
    }
    return t
}

function m(t) {
    for (var e = t.size, r = t.num, n = d, o = n(340), i = function (t, e) {
        return t | e
    }, a = r, u = ""; e--;) if (o === n(329)) {
        var c = _$o.random() * (_$d.length - _$L) | 0;
        _$Y += _$V[c], _$M[c] = _$x[_$R.length - _$W - 1]
    } else u += a[i(Math.random() * a.length, 0)];
    return u
}

function genFingerPrint() {
    var t = d, r = t(335), n = y(r, 4), o = g(), i = _(r, n), a = ((m({
        size: o, num: i
    }) + n + m({
        size: ((12 - o)) - 1, num: i
    })) + o).split(""), u = a.slice(0, 8), h = a.slice(8), p = [];
    for (; u.length > 0;) {
        p.push((35 - parseInt(u.pop(), 36)).toString(36))
    }
    return (p = p.concat(h)).join("")

}

console.info(genFingerPrint())