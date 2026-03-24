#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys

FILE_NAME = 'TWTB4U.csv'

# 用 Big5 (cp950) 解碼
with open(FILE_NAME, 'rb') as f:
    content = f.read().decode('cp950')

# 寫回檔案讓 csv module 讀取
import io
reader = csv.reader(io.StringIO(content))

stock_list = []
count = 0
for row in reader:
    count += 1
    # 跳過前幾行標題，找到股票代號欄位
    if len(row) >= 2 and count > 8:
        stock_id = row[0].strip()
        # 只取數字或數字+字母的代號（排除空白行）
        if stock_id and stock_id[0].isdigit():
            stock_list.append(stock_id)

# 寫入 stocknumber.csv
with open('stocknumber.csv', 'w', encoding='utf-8', newline='') as f:
    cw = csv.writer(f)
    for stock_index in stock_list:
        cw.writerow([stock_index])

print(f"已更新 stocknumber.csv，共 {len(stock_list)} 檔股票")
print("前10檔:", stock_list[:10])
