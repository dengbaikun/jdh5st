import hashlib
import json
import os
import pickle
import random
import subprocess
import time
import copy

import execjs
import requests
from Crypto.Cipher import AES

from utils.codec_utils import HEX
from utils.digester_utils import Digester
from datetime import datetime
from datetime import timezone, timedelta

from utils.symmetric_crypto_utils import SymmetricCrypto


class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(encoding='UTF-8', *args, **kwargs)


subprocess.Popen = MySubprocessPopen


def generate_random_code(length):
    char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'
    """
    生成一个指定长度的随机字符串。

    :param char_set: 用于生成随机码的字符集。
    :param length: 随机字符串的长度。
    :return: 生成的随机字符串。
    """
    return ''.join(random.choice(char_set) for _ in range(length))


def gen_sign(key, t):
    data = '&'.join([f'{item["key"]}:{item["value"]}' for item in t])
    result = Digester.md5(f'{key}{data}{key}')
    return result


class H5ST(object):
    def __init__(self, skuId):
        self.sku_id = skuId
        self.appid = 'fb5df'
        self.version = '4.4'
        self.algo = None
        self.fingerPrint = None
        self.token = None
        self.algo_dir_path = './algo/'

    def encrypt_env(self):
        aes_iv = '0102030405060708'
        aes_key = 'r1T.6Vinpb.k+/a)'
        env_data = {
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
            "random": generate_random_code(11),
            "v": "h5_file_v4.4.0",
            "fp": self.fingerPrint,
            "bu1": "0.1.8"
        }

        key = aes_key.encode('utf8')
        iv = aes_iv.encode('utf8')
        data = json.dumps(env_data, indent=2)
        plaintext = data.encode('utf8')
        ciphertext = SymmetricCrypto.encrypt_aes(key, plaintext, AES.MODE_CBC, HEX, iv)
        return ciphertext

    def gen_key(self, u):
        nodejs = '''
        const CryptoJS = require('crypto-js');
        const cryptojs= {
            HmacMD5: function (text, secret){return CryptoJS.HmacMD5(text,secret).toString()},
            HmacSHA256: function (text, secret){return CryptoJS.HmacSHA256(text, secret).toString()},
            HmacSHA512: function (text, secret){return CryptoJS.HmacSHA512(text, secret).toString()},
            MD5: function (text){return CryptoJS.MD5(text).toString()},
            SHA256: function (text){return CryptoJS.SHA256(text).toString()},
            SHA512: function (text){return CryptoJS.SHA512(text).toString()},
        }
        function genKey(tk,fp,ts,ai){
            return fn(tk,fp,ts,ai,cryptojs)
        }
        '''
        nodejs = f'{nodejs}\n const fn = {self.algo}'
        return execjs.compile(nodejs).call("genKey", self.token, self.fingerPrint, u, self.appid)

    def gen_h5st(self, l):
        if self.load_algo_to_local() is None:
            self.get_algo()
        # 先获取对象的所有键，并按字母顺序排序
        t = [{'key': k, 'value': l[k]} for k in sorted(l.keys())]
        # 给定的时间戳（毫秒）
        timestamp_ms = int(time.time() * 1000)
        # 将时间戳转换为datetime对象（假设时间戳是基于UTC的）
        dt = datetime.utcfromtimestamp(timestamp_ms / 1000.0)
        beijing_time = dt.replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
        # 格式化时间
        date_time = beijing_time.strftime("%Y%m%d%H%M%S%f")[:17]  # 包括毫秒的前17个字符
        print(f"date_time={date_time}")
        u = date_time + '88'
        print(f"u={u}")
        env_data = self.encrypt_env()
        print(f'encrypt_env={env_data}')
        key = self.gen_key(u)
        print(f'key={key}')
        sign = gen_sign(key, t)
        print(f'sign={sign}')
        h5st = f'{date_time};{self.fingerPrint};{self.appid};{self.token};{sign};{self.version};{timestamp_ms};{env_data}'
        print(f'h5st={h5st}')
        return h5st

    def save_algo_to_local(self, algo):
        algo_file = '{}{}.algo'.format(self.algo_dir_path, 'algo')
        directory = os.path.dirname(algo_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(algo_file, 'wb') as f:
            pickle.dump(algo, f)

    def load_algo_to_local(self):
        algo_file = ''
        if not os.path.exists(self.algo_dir_path):
            return None
        for name in os.listdir(self.algo_dir_path):
            if name.endswith(f".algo"):
                algo_file = '{}{}'.format(self.algo_dir_path, name)
                break
        if algo_file == '':
            return None
        with open(algo_file, 'rb') as f:
            algo_file = pickle.load(f)
            self.algo = algo_file['algo']
            self.token = algo_file['token']
            self.fingerPrint = algo_file['fingerPrint']
        return algo_file

    def get_algo(self):
        headers = {
            "authority": "cactus.jd.com",
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/json",
            "origin": "https://item.jd.com",
            "referer": f"https://item.jd.com/{self.sku_id}.html",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        url = "https://cactus.jd.com/request_algo"
        params = {
            "g_ty": "ajax"
        }
        with open('fingerPrint.js', encoding='utf-8') as f:
            js = f.read()
        fp = execjs.compile(js).call("genFingerPrint")

        key = 'wm0!@w-s#ll1flo('
        iv = '0102030405060708'
        env = {
            "wc": 0,
            "wd": 0,
            "l": "zh-CN",
            "ls": "zh-CN,zh",
            "ml": 2,
            "pl": 5,
            "av": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
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
                "bu2": 0,
                "bu3": 92,
                "bu4": 0,
                "bu5": 0
            },
            "pp1": "",
            "bu1": "",
            "w": 1920,
            "h": 1080,
            "ow": 160,
            "oh": 28,
            "url": "https://item.jd.com/100071422470.html",
            "og": "https://item.jd.com",
            "pr": 1,
            "re": "https://cfe.m.jd.com/",
            "random": generate_random_code(11),
            "referer": "https://cfe.m.jd.com/",
            "v": "h5_file_v4.4.0",
            "ai": "fb5df",
            "fp": fp
        }
        key = key.encode('utf8')
        iv = iv.encode('utf8')
        data = json.dumps(env, indent=2)
        plaintext = data.encode('utf8')
        ciphertext = SymmetricCrypto.encrypt_aes(key, plaintext, AES.MODE_CBC, HEX, iv)
        data = {
            "version": "4.4",
            "fp": fp,
            "appId": "fb5df",
            "timestamp": int(time.time() * 1000),
            "platform": "web",
            "expandParams": ciphertext,
            "fv": "h5_file_v4.4.0"
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, params=params, data=data)
        resp_dict = json.loads(response.text)
        result = resp_dict['data']['result']
        token = result['tk']
        algo = result['algo']
        fingerPrint = result['fp']
        print(f'token={token}\nalgo={algo}\nfingerPrint={fingerPrint}')
        algo_file = {'token': token, 'algo': algo, 'fingerPrint': fingerPrint}
        self.algo = algo
        self.token = token
        self.fingerPrint = fingerPrint
        self.save_algo_to_local(algo_file)
        return fingerPrint, token, algo


