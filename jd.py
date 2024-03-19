import re
import time
from utils.digester_utils import Digester
import execjs
import requests
import json5
import json
import subprocess
import copy
class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(encoding='UTF-8', *args, **kwargs)


subprocess.Popen = MySubprocessPopen
import execjs
headers = {
    "authority": "api.m.jd.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://item.jd.com",
    "referer": "https://item.jd.com/100011293139.html",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "x-referer-page": "https://item.jd.com/100011293139.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "166875052289262543994",
    "shshshfpa": "b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789",
    "shshshfpx": "b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789",
    "TrackID": "14PF-dEiQugVUN_eiTWYCAVQBLDPhOhuDiYRkG6F5BfeN2ZMxTXfOVZnYRuKXNqqquavtQcGzeOeNr5IS2h3yafBoO_P42HzY3v8q-ewLj9w",
    "thor": "8F5208C9AC0E50DD03ADBF4B4BC693F7611F10288F3B374DEFC49B3F5295D77E16C113850F074D83C335412C0B13FD03983D9B43D1C6BC5833318B71E39EE7E94DBF6263DCD8672DBA49697CEF10A765900894C05EF4551A244753B30ED0C80B0C8E5412295485DE58869E70B1CFC8E4ECBE94FEEB98D8EFEA4EE0928C2D68BC8213658AC444E2BEC5252ACEFB88F6E69C33B8B0C49FC9341425CBD833F971D7",
}
url = "https://item.jd.com/100011293139.html"
response = requests.get(url, headers=headers, cookies=cookies)
# 确保请求成功
if response.status_code == 200:
    # 查找'var pageConfig'变量
    match = re.search(r'var pageConfig = ({.*?});', response.text, re.DOTALL)
    if match:
        # 提取变量的值
        page_config_str = match.group(1)
        pageConfig = json5.loads(page_config_str)
        print(f"pageConfig={pageConfig}")
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
            't': int(time.time()*1000),
            'body': json.dumps(body, separators=(',', ':')),
        }
        sha256_body = Digester.sha256(params['body'])
        d = copy.deepcopy(params)
        d['body'] = sha256_body
        with open('getH5st.js', encoding='utf-8') as f:
            js = f.read()
        h5st = execjs.compile(js).call("getH5st", d)
        print(f'h5st={h5st}')
        url = "https://api.m.jd.com/"
        params['h5st'] = h5st
        params['loginType'] = '3'
        params['scval'] = '100011293139'
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        print(response.text)
        print(response)
    else:
        print("无法找到'var pageConfig'变量。")
else:
    print(f"请求失败，状态码：{response.status_code}")
