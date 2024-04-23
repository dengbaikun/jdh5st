import os
import pickle
import re
import time
from h5st import H5ST
from Crypto.Cipher import AES

from utils.codec_utils import HEX
from utils.digester_utils import Digester
import execjs
import requests
import json5
import json
import subprocess
import copy
import random
from utils.symmetric_crypto_utils import SymmetricCrypto
from utils.timer import Timer


class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(encoding='UTF-8', *args, **kwargs)


subprocess.Popen = MySubprocessPopen


class Jd(object):
    def __init__(self):
        self.sku_id = 100071422470
        self.page_config_dir_path = './page_config/'
        self.headers = {
            "authority": "api.m.jd.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "origin": "https://item.jd.com",
            "referer": "https://item.jd.com/100071422470.html",
            "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "x-referer-page": "https://item.jd.com/10096186210939.html",
            "x-rp-client": "h5_1.0.0"
        }
        self.cookies = {
            "__jdu": "166875052289262543994",
            "shshshfpa": "b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789",
            "shshshfpx": "b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789",
            "TrackID": "14PF-dEiQugVUN_eiTWYCAVQBLDPhOhuDiYRkG6F5BfeN2ZMxTXfOVZnYRuKXNqqquavtQcGzeOeNr5IS2h3yafBoO_P42HzY3v8q-ewLj9w",
            "thor": "8F5208C9AC0E50DD03ADBF4B4BC693F7611F10288F3B374DEFC49B3F5295D77E16C113850F074D83C335412C0B13FD03983D9B43D1C6BC5833318B71E39EE7E94DBF6263DCD8672DBA49697CEF10A765900894C05EF4551A244753B30ED0C80B0C8E5412295485DE58869E70B1CFC8E4ECBE94FEEB98D8EFEA4EE0928C2D68BC8213658AC444E2BEC5252ACEFB88F6E69C33B8B0C49FC9341425CBD833F971D7",
        }
        self.session = requests.Session()
        # 设置重试次数 设置线程池
        self.timeout = 5

    def save_page_config_to_local(self, page_config):
        cookies_file = '{}{}.page_config'.format(self.page_config_dir_path, self.sku_id)
        directory = os.path.dirname(cookies_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(cookies_file, 'wb') as f:
            pickle.dump(page_config, f)

    def load_page_config(self):
        page_config_file = ''
        if not os.path.exists(self.page_config_dir_path):
            return None
        for name in os.listdir(self.page_config_dir_path):
            if name.endswith(f"{self.sku_id}.page_config"):
                page_config_file = '{}{}'.format(self.page_config_dir_path, name)
                break
        if page_config_file == '':
            return None
        with open(page_config_file, 'rb') as f:
            page_config = pickle.load(f)
        return page_config

    @Timer('get_page_config')
    def get_page_config(self):
        page_config = self.load_page_config()
        if page_config is not None:
            return page_config
        url = f"https://item.jd.com/{self.sku_id}.html"
        response = self.session.get(url, headers=self.headers)
        # 确保请求成功
        if response.status_code == 200:
            # 查找'var pageConfig'变量
            match = re.search(r'var pageConfig = ({.*?});', response.text, re.DOTALL)
            if match:
                # 提取变量的值
                page_config_str = match.group(1)
                pageConfig = json5.loads(page_config_str)
                self.save_page_config_to_local(pageConfig)
                return pageConfig
            else:
                print("无法找到'var pageConfig'变量。")

    @Timer('getPcItemSoa')
    def getPcItemSoa(self):
        pageConfig = self.get_page_config()
        body = {
            'skuId': pageConfig['product']['skuid'],
            'cat': ','.join([str(cat) for cat in pageConfig['product']['cat']]),
            'area': '19_1666_36267_36272',
            'shopId': pageConfig['product']['shopId'],
            'venderId': pageConfig['product']['venderId'],
            'paramJson': pageConfig['product']['paramJson'],
            'num': int(pageConfig['product']['countNum'] if 'countNum' in pageConfig['product'] else "1"),
            'bbTraffic': '',
            'canvasType': 1
        }
        params = {
            'appid': "pc-item-soa",
            'functionId': "pc_detailpage_wareBusiness",
            'client': "pc",
            'clientVersion': "1.0.0",
            't': int(time.time() * 1000),
            'body': json.dumps(body, separators=(',', ':')),
        }
        sha256_body = Digester.sha256(params['body'])
        d = copy.deepcopy(params)
        d['body'] = sha256_body
        h5st = H5ST(self.sku_id)
        h5st = h5st.gen_h5st(d)
        params['h5st'] = h5st
        params['loginType'] = '3'
        params['scval'] = '100011293139'
        url = "https://api.m.jd.com/"
        response = self.session.get(url, headers=self.headers, cookies=self.cookies, params=params)
        print(response.text)
        print(response)


if __name__ == '__main__':
    show = '''
                                                               ii.                                         ;9ABH,
                                                          SA391,                                    .r9GG35&G
                                                          &#ii13Gh;                               i3X31i;:,rB1
                                                          iMs,:,i5895,                         .5G91:,:;:s1:8A
                                                           33::::,,;5G5,                     ,58Si,,:::,sHX;iH1
                                                            Sr.,:;rs13BBX35hh11511h5Shhh5S3GAXS:.,,::,,1AG3i,GG
                                                            .G51S511sr;;iiiishS8G89Shsrrsh59S;.,,,,,..5A85Si,h8
                                                           :SB9s:,............................,,,.,,,SASh53h,1G.
                                                        .r18S;..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,....,,.1H315199,rX,
                                                      ;S89s,..,,,,,,,,,,,,,,,,,,,,,,,....,,.......,,,;r1ShS8,;Xi
                                                    i55s:.........,,,,,,,,,,,,,,,,.,,,......,.....,,....r9&5.:X1
                                                   59;.....,.     .,,,,,,,,,,,...        .............,..:1;.:&s
                                                  s8,..;53S5S3s.   .,,,,,,,.,..      i15S5h1:.........,,,..,,:99
                                                  93.:39s:rSGB@A;  ..,,,,.....    .SG3hhh9G&BGi..,,,,,,,,,,,,.,83
                                                  G5.G8  9#@@@@@X. .,,,,,,.....  iA9,.S&B###@@Mr...,,,,,,,,..,.;Xh
                                                  Gs.X8 S@@@@@@@B:..,,,,,,,,,,. rA1 ,A@@@@@@@@@H:........,,,,,,.iX:
                                                 ;9. ,8A#@@@@@@#5,.,,,,,,,,,... 9A. 8@@@@@@@@@@M;    ....,,,,,,,,S8
                                                 X3    iS8XAHH8s.,,,,,,,,,,...,..58hH@@@@@@@@@Hs       ...,,,,,,,:Gs
                                                r8,        ,,,...,,,,,,,,,,.....  ,h8XABMMHX3r.          .,,,,,,,.rX:
                                               :9, .    .:,..,:;;;::,.,,,,,..          .,,.               ..,,,,,,.59
                                              .Si      ,:.i8HBMMMMMB&5,....                    .            .,,,,,.sMr
                                              SS       :: h@@@@@@@@@@#; .                     ...  .         ..,,,,iM5
                                              91  .    ;:.,1&@@@@@@MXs.                            .          .,,:,:&S
                                              hS ....  .:;,,,i3MMS1;..,..... .  .     ...                     ..,:,.99
                                              ,8; ..... .,:,..,8Ms:;,,,...                                     .,::.83
                                               s&: ....  .sS553B@@HX3s;,.    .,;13h.                            .:::&1
                                                SXr  .  ...;s3G99XA&X88Shss11155hi.                             ,;:h&,
                                                 iH8:  . ..   ,;iiii;,::,,,,,.                                 .;irHA
                                                  ,8X5;   .     .......                                       ,;iihS8Gi
                                                     1831,                                                 .,;irrrrrs&@
                                                       ;5A8r.                                            .:;iiiiirrss1H
                                                         :X@H3s.......                                .,:;iii;iiiiirsrh
                                                          r#h:;,...,,.. .,,:;;;;;:::,...              .:;;;;;;iiiirrss1
                                                         ,M8 ..,....,.....,,::::::,,...         .     .,;;;iiiiiirss11h
                                                         8B;.,,,,,,,.,.....          .           ..   .:;;;;iirrsss111h
                                                        i@5,:::,,,,,,,,.... .                   . .:::;;;;;irrrss111111
                                                        9Bi,:,,,,......                        ..r91;;;;;iirrsss1ss1111

        '''
    print(show)
    jd = Jd()
    jd.getPcItemSoa()
