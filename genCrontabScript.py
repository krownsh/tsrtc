#!/usr/bin/python
# -*- coding: utf-8 -*-

# 產生開盤時間每分鐘跑一次 crawl.py 的 crontab
# 台股交易時間：週一至週五 09:00-13:30（中午不休息）

import os

# 改成你實際的路徑
CRAWL_PATH = '/Users/kangjunxuan/.openclaw/workspace/tsrtc_stock_intrady_detail'
PYTHON_PATH = '/usr/bin/python3'

print("# 台股即時行情監測 - Crontab")
print("# 每天開盤時間每分鐘抓一次 (09:00-13:30)")
print()

# 09:00-13:30，每分鐘
for hour in range(9, 14):
    if hour == 13:
        # 13:00-13:30 (0-29 分)
        for minute in range(30):
            print(f'{minute} {hour} * * 1-5 ( cd {CRAWL_PATH} && {PYTHON_PATH} crawl.py )')
    else:
        # 09:00-12:59 (0-59 分)
        for minute in range(60):
            print(f'{minute} {hour} * * 1-5 ( cd {CRAWL_PATH} && {PYTHON_PATH} crawl.py )')

print()
print("# 若要每5秒跑一次，請用：")
print("# */5 * * * 1-5 ( cd {CRAWL_PATH} && {PYTHON_PATH} crawl.py )")
