# -*- coding: utf-8 -*-
import logging.handlers
import random
import time

import requests
import pprint


def init_logger(logger_name, debug=False):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")
    logfile = "/home/t/var/log/coin_price.log"
    if not logger.handlers:
        rotate_handle = logging.handlers.RotatingFileHandler(
            logfile, maxBytes=1024 * 1024 * 50, backupCount=3, encoding="utf-8"
        )
        rotate_handle.setFormatter(formatter)
        logger.addHandler(rotate_handle)

        if debug:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
    return logger

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Cookie': 'cookie_name=cookie_value',
}


proxy = {
    'http': 'http://t:2340',  # HTTP 代理
    'https': 'http://t:2340',  # HTTPS 代理
}

url = "https://fxhapi.feixiaohao.com/public/v1/ticker?start=0&limit=80"

log = init_logger("coin", debug=True)

def get_data():
    data = requests.get(url, headers=headers, proxies=proxy)
    for coin in data.json():
        symbol = coin.get("symbol")
        if symbol in ("MINA", "FIL", "BTC"):
            price = coin.get("price_usd")
            # pprint.pprint(coin)
            msg = f"{symbol} {price}"
            log.info(msg)

if __name__ == "__main__":
    while True:
        try:
            get_data()
        except Exception as ex:
            log.warning(f"something went wrong {ex}")
            time.sleep(10)
        time.sleep(random.randint(3, 7) * 60)
