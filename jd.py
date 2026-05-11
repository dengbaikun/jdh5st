import copy
import json
import os
import re
import subprocess
import sys
import time
from urllib.parse import urlparse

import json5
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from h5st import H5ST
from utils.digester_utils import Digester


class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(encoding='UTF-8', *args, **kwargs)


subprocess.Popen = MySubprocessPopen


def extract_sku_id(item_url: str) -> str:
    parsed = urlparse(item_url)
    if 'jd.com' not in parsed.netloc:
        raise ValueError(f'无效的京东商品链接: {item_url}')
    match = re.search(r'/([0-9]{6,})\.html', parsed.path)
    if not match:
        raise ValueError(f'商品链接中未找到 skuId: {item_url}')
    return match.group(1)


def build_session() -> requests.Session:
    session = requests.Session()
    # 避免使用环境里的代理变量，减少被代理拦截导致 403。
    session.trust_env = False
    retries = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=0.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(['GET'])
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session


def parse_cookie_string(cookie_string: str) -> dict:
    cookie_dict = {}
    for item in cookie_string.split(';'):
        if '=' not in item:
            continue
        key, value = item.split('=', 1)
        cookie_dict[key.strip()] = value.strip()
    return cookie_dict


def main():
    item_url = sys.argv[1] if len(sys.argv) > 1 else 'https://item.jd.com/100011293139.html'
    sku_id = extract_sku_id(item_url)

    headers = {
        'authority': 'api.m.jd.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://item.jd.com',
        'referer': f'https://item.jd.com/{sku_id}.html',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-referer-page': f'https://item.jd.com/{sku_id}.html',
        'x-rp-client': 'h5_1.0.0'
    }
    cookies = {
        '__jdu': '166875052289262543994',
        'shshshfpa': 'b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789',
        'shshshfpx': 'b679439f-c6b7-12a0-4ea4-fc91a6b9d991-1656387789',
        'TrackID': '14PF-dEiQugVUN_eiTWYCAVQBLDPhOhuDiYRkG6F5BfeN2ZMxTXfOVZnYRuKXNqqquavtQcGzeOeNr5IS2h3yafBoO_P42HzY3v8q-ewLj9w',
        'thor': '8F5208C9AC0E50DD03ADBF4B4BC693F7611F10288F3B374DEFC49B3F5295D77E16C113850F074D83C335412C0B13FD03983D9B43D1C6BC5833318B71E39EE7E94DBF6263DCD8672DBA49697CEF10A765900894C05EF4551A244753B30ED0C80B0C8E5412295485DE58869E70B1CFC8E4ECBE94FEEB98D8EFEA4EE0928C2D68BC8213658AC444E2BEC5252ACEFB88F6E69C33B8B0C49FC9341425CBD833F971D7',
    }

    # 优先使用你自己的最新浏览器 Cookie，防止京东风控识别到旧 Cookie。
    env_cookie = os.getenv('JD_COOKIE', '').strip()
    if env_cookie:
        cookies = parse_cookie_string(env_cookie)
        print('已使用环境变量 JD_COOKIE 覆盖默认 Cookie。')
    else:
        print('未设置 JD_COOKIE，正在使用仓库内置 Cookie（可能触发风控）。')

    session = build_session()

    try:
        response = session.get(f'https://item.jd.com/{sku_id}.html', headers=headers, cookies=cookies, timeout=15)
    except requests.RequestException as exc:
        print(f'请求商品页失败: {exc}')
        return

    if response.status_code != 200:
        print(f'请求失败，状态码：{response.status_code}')
        return

    match = re.search(r'var pageConfig = ({.*?});', response.text, re.DOTALL)
    if not match:
        print("无法找到'var pageConfig'变量。")
        return

    page_config = json5.loads(match.group(1))
    print(f'pageConfig={page_config}')

    body = {
        'skuId': page_config['product']['skuid'],
        'cat': ','.join([str(cat) for cat in page_config['product']['cat']]),
        'area': '19_1666_36267_36272',
        'shopId': page_config['product']['shopId'],
        'venderId': page_config['product']['venderId'],
        'paramJson': page_config['product']['paramJson'],
        'num': int(page_config['product'].get('countNum', '1')),
        'bbTraffic': '',
        'canvasType': 1
    }
    params = {
        'appid': 'pc-item-soa',
        'functionId': 'pc_detailpage_wareBusiness',
        'client': 'pc',
        'clientVersion': '1.0.0',
        't': int(time.time() * 1000),
        'body': json.dumps(body, separators=(',', ':')),
    }

    d = copy.deepcopy(params)
    d['body'] = Digester.sha256(params['body'])
    # 优先使用 h5st.py 中较新的算法流程（会先请求 cactus 的 algo/token）。
    # 避免 getH5st.js 版本滞后导致签名与当前风控不匹配。
    h5st = H5ST(int(sku_id)).gen_h5st(d)

    params['h5st'] = h5st
    params['loginType'] = '3'
    params['scval'] = sku_id
    try:
        detail_response = session.get('https://api.m.jd.com/', headers=headers, cookies=cookies, params=params, timeout=15)
    except requests.RequestException as exc:
        print(f'请求详情接口失败: {exc}')
        return

    print(detail_response.text)
    print(detail_response)
    if '请进行验证' in detail_response.text or '验证码' in detail_response.text or 'antiCrawler' in detail_response.text:
        print('检测到疑似风控拦截：请更新 JD_COOKIE 后重试。')


if __name__ == '__main__':
    main()
