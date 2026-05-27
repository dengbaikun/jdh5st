import copy
import json
import logging
import os
import pickle
import re
import time

import json5
import requests

from h5st import H5ST
from utils import config
from utils.timer import Timer


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


class Jd(object):
    def __init__(self):
        self.sku_id = config.SKU_ID
        self.area = config.AREA
        self.page_config_dir_path = config.PAGE_CONFIG_DIR
        self.session = requests.Session()
        self.timeout = 10
        self.headers = self.build_headers()
        self.session.cookies.update(config.parse_cookie_string(config.JD_COOKIE))

    def build_headers(self):
        return {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://item.jd.com",
            "priority": "u=1, i",
            "referer": f"https://item.jd.com/{self.sku_id}.html",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": config.USER_AGENT,
            "x-referer-page": f"https://item.jd.com/{self.sku_id}.html",
            "x-rp-client": "h5_2.2.0",
        }

    def save_page_config_to_local(self, page_config):
        page_config_file = os.path.join(self.page_config_dir_path, f"{self.sku_id}.page_config")
        directory = os.path.dirname(page_config_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(page_config_file, "wb") as f:
            pickle.dump(page_config, f)

    def load_page_config(self):
        page_config_file = os.path.join(self.page_config_dir_path, f"{self.sku_id}.page_config")
        if not config.USE_PAGE_CACHE or not os.path.exists(page_config_file):
            return None
        with open(page_config_file, "rb") as f:
            return pickle.load(f)

    @Timer("get_page_config")
    def get_page_config(self):
        page_config = self.load_page_config()
        if page_config is not None:
            return page_config

        url = f"https://item.jd.com/{self.sku_id}.html"
        response = self.session.get(url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()

        match = re.search(r"var pageConfig = ({.*?});", response.text, re.DOTALL)
        if not match:
            raise RuntimeError("Cannot find 'var pageConfig' in item page.")

        page_config = json5.loads(match.group(1))
        self.save_page_config_to_local(page_config)
        return page_config

    def build_body(self, page_config):
        product = page_config["product"]
        return {
            "skuId": product["skuid"],
            "cat": ",".join([str(cat) for cat in product["cat"]]),
            "area": self.area,
            "shopId": product["shopId"],
            "venderId": product["venderId"],
            "paramJson": product["paramJson"],
            "num": int(product["countNum"] if "countNum" in product else "1"),
            "bbTraffic": "",
            "canvasType": 1,
        }

    def build_params(self, body):
        params = {
            "appid": "pc-item-soa",
            "functionId": "pc_detailpage_wareBusiness",
            "client": "pc",
            "clientVersion": "1.0.0",
            "t": int(time.time() * 1000),
            "body": json.dumps(body, separators=(",", ":")),
        }
        optional_params = {
            "uuid": config.JD_UUID,
            "x-api-eid-token": config.JD_EID_TOKEN,
            "loginType": config.JD_LOGIN_TYPE,
            "scval": config.JD_SCVAL,
        }
        params.update({key: value for key, value in optional_params.items() if value})
        return params

    def apply_browser_cookies(self, signed_params):
        for cookie in signed_params.get("__cookies", []):
            self.session.cookies.set(
                cookie["name"],
                cookie["value"],
                domain=cookie.get("domain"),
                path=cookie.get("path", "/"),
            )

    def handle_risk_control(self, response):
        sd_token = response.headers.get("X-Rp-Sdtoken", "")
        request_id = response.headers.get("X-API-Request-Id", "")
        if response.status_code != 403 or not sd_token:
            return False

        logger.warning("api.m.jd.com returned 403 and triggered JD risk control.")
        logger.warning("X-API-Request-Id: %s", request_id)
        logger.warning("X-Rp-Sdtoken prefix: %s", sd_token[:80])
        logger.warning("Stop retrying this private endpoint; use the official JD API / authorized business API.")
        return True

    def log_response(self, response, signed_params):
        h5st = signed_params.get("h5st", "")
        h5st_version = h5st.split(";")[5] if h5st.count(";") >= 5 else "unknown"
        logger.info(
            "status=%s request_id=%s h5st_version=%s stk=%s",
            response.status_code,
            response.headers.get("X-API-Request-Id", ""),
            h5st_version,
            signed_params.get("_stk", ""),
        )

    @Timer("getPcItemSoa")
    def getPcItemSoa(self):
        page_config = self.get_page_config()
        body = self.build_body(page_config)
        params = self.build_params(body)

        h5st = H5ST(self.sku_id)
        signed_params = h5st.sign_params(copy.deepcopy(params))
        self.apply_browser_cookies(signed_params)
        params.update({
            "_stk": signed_params.get("_stk"),
            "_ste": signed_params.get("_ste"),
            "h5st": signed_params["h5st"],
        })

        response = self.session.get(
            "https://api.m.jd.com/",
            headers=self.headers,
            params=params,
            timeout=self.timeout,
        )
        self.log_response(response, signed_params)
        if self.handle_risk_control(response):
            return response

        logger.info("response body: %s", response.text)
        return response


if __name__ == "__main__":
    jd = Jd()
    jd.getPcItemSoa()
