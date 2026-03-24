#!/usr/bin/python
# -*- coding: utf-8 -*-

# 產生開盤時間每5分鐘跑一次 crawl.py 的 crontab
# 台股交易時間：週一至週五 09:00-12:00, 13:30-13:30

import os
import sys

# 改成你實際的路徑
CRAWL_PATH = '/Users/kangjunxuan/.openclaw/workspace/tsrtc_stock_intrady_detail'
PYTHON_PATH = '/usr/bin/python3'

print("# 台股即時行情監測 - Crontab")
print("# 每天開盤時間每分鐘抓一次")

# 09:00-12:00，每分鐘
for minute in range(60):
    print(f'{minute} 9 * * 1-5 ( cd {CRAWL_PATH} && {PYTHON_PATH} crawl.py )')

# 13:30-13:59，每分鐘  
for minute in range(30):
    print(f'{minute} 13 * * 1-5 ( cd {CRAWL_PATH} && {PYTHON_PATH} crawl.py )')

print("# 以上是每分鐘跑一次，若要每5秒跑一次請用以下設定：")
print("# */5 * * * 1-5 ( cd /path/to/tsrtc && python3 crawl.py )")
