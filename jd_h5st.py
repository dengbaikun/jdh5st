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
        kwargs.setdefault('encoding', 'UTF-8')
        super().__init__(*args, **kwargs)


subprocess.Popen = MySubprocessPopen


class Jd(object):
    def __init__(self):
        self.sku_id = 100071422470
        self.page_config_dir_path = './page_config/'
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://item.jd.com",
            "priority": "u=1, i",
            "referer": "https://item.jd.com/",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
            "x-referer-page": f"https://item.jd.com/{self.sku_id}.html",
            "x-rp-client": "h5_2.2.0"
        }
        self.cookies = {
        "__jdv": "122270672%7Cdirect%7C-%7Cnone%7C-%7C1779787739916",
        "mba_muid": "17797877399161687594981",
        "__jdu": "17797877399161687594981",
        "3AB9D23F7A4B3CSS": "jdd03QUZ7OUOAYKI7QQEVOPIOVFIXFPPT2J4CDGYOKROZ4BW7JGAZVE2R444CHVNCPGCAIZWHGCFY6U7E2SYL5O2ZVFTVRUAAAAM6MO22RAAAAAAADOUQSPLLP2UXWUX",
        "_gia_d": "1",
        "areaId": "19",
        "ipLoc-djd": "19-1666-0-0",
        "mba_sid": "1779787739917512077496.3",
        "wlfstk_smdl": "bb3pnlvsxanrmqkjx6iwclc4e73q9lcl",
        "3AB9D23F7A4B3C9B": "QUZ7OUOAYKI7QQEVOPIOVFIXFPPT2J4CDGYOKROZ4BW7JGAZVE2R444CHVNCPGCAIZWHGCFY6U7E2SYL5O2ZVFTVRU",
        "TrackID": "1B5i2AGF3C2bfwq8wYxBQW2hiRGhP300sGnkrmWyEGfpNftqLITfWyMjgymfCY8OEpcDvqSG0oWnZMgXDYy8I1NX-jK7ZX9-zYMXaebzGbXLIaa7tSVPDXbSPU2qB_LGw",
        "thor": "8F5208C9AC0E50DD03ADBF4B4BC693F7611F10288F3B374DEFC49B3F5295D77EF796AB3AE74D178983CB6AFBD136498285FCD820FCA72EE77135E9EFFD0FEC9C3A9EE85946CF4390302C88D445D989C193E8C791EE6C1CDFE4F94C0BF314D8DF1FBB795B73B1F81F1E30435F0083D02BE3BB373BDEE64E134258EC1C0B8DA8FD47C9B7CEEE4FE20F3CD7F4E3CF77DB6FD8C8F430A57F93038C809F17C40886C7",
        "flash": "3_4UhiZWxIfY3lHqZg0VnD2oWvzdeBpjXQJB_BWLBdniyr5TdRfv_Up6OWl-ihtjQsnsY_ZgHgR-E0IyICQn9QgLa5k_Xzp-8ZUmABH1nHSjiIkGcuJLOLpz3k0oI0DrRxCaAeQabOft2CgOaxGSBT70CF1Y-vY20MkHaq8wOoLYxb5BlUsAMwLV**",
        "light_key": "AASBKE7rOxgWQziEhC_QY6yacE67_EmlNYs4g-udV6lST7ArLpiUyvTcVyOkGnT_rg1s6dSC",
        "pinId": "iUhfo8tVoA0orkmEvSwKULV9-x-f3wj7",
        "pin": "jd_4536d74677e8d",
        "unick": "jd_132884ger",
        "ceshi3.com": "201",
        "_tp": "cuf1PxPHod0x5ppVA3nVM9web9%2FU6cZkZBtOlsaQ6to%3D",
        "_pst": "jd_4536d74677e8d",
        "token": "c7f0b39c7a75d65f167f764fc9446c13,3,988771",
        "__jda": "181111935.17797877399161687594981.1779787739.1779787739.1779787739.1",
        "__jdc": "181111935",
        "cn": "21",
        "shshshfpa": "6a8a53ed-588e-93cb-dae0-dc4f575821a5-1779789339",
        "shshshfpx": "6a8a53ed-588e-93cb-dae0-dc4f575821a5-1779789339",
        "shshshfpb": "BApXWvLS-YPtAfP39qsl9f2gptTjsnpB_Bjs5lBZo9xJ1ItZfQtKDwUzv23-sZNF2K7EluNSNsqFbdOk0v64Nt48vMV_jqTWVa99h",
        "RT": "\"z=1&dm=jd.com&si=wx499ie8x8j&ss=mpmglnvc&sl=3&tt=0&obo=3\"",
        "__jdb": "181111935.17.17797877399161687594981|1.1779787739",
        "sdtoken": "AAbEsBpEIOVjqTAKCQtvQu17DQqoeLpqs6gENlT6pqqsukjeocBElw0EHcIM2--z0ue-vyXp0WXt3hsYrzL4IOtBnvxeE40ChaA9xTCfUsJF9aGumYGoHzDJIkb-idtSFuOjVnde"
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
        h5st = H5ST(self.sku_id)
        params = {
            "uuid": "17797877399161687594981",
            'appid': "pc-item-soa",
            'functionId': "pc_detailpage_wareBusiness",
            'client': "pc",
            "uuid": "17797877399161687594981",
            'clientVersion': "1.0.0",
            't': int(time.time() * 1000),
            'body': json.dumps(body, separators=(',', ':')),
            "x-api-eid-token": "jdd03QUZ7OUOAYKI7QQEVOPIOVFIXFPPT2J4CDGYOKROZ4BW7JGAZVE2R444CHVNCPGCAIZWHGCFY6U7E2SYL5O2ZVFTVRUAAAAM6MO22RAAAAAAADOUQSPLLP2UXWUX"
        }
        # params['scval'] = '100011293139'
        signed_params = h5st.sign_params(copy.deepcopy(params))
        for cookie in signed_params.get('__cookies', []):
            self.session.cookies.set(cookie['name'], cookie['value'], domain=cookie.get('domain'))
        params.update({
            # '_stk': signed_params['_stk'],
            # '_ste': signed_params['_ste'],
            'h5st': signed_params['h5st']
        })
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
