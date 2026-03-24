#!/bin/python
# -*- coding: utf-8 -*-

import csv
import os
from os import listdir
from os.path import join
from datetime import date

today = str(date.today().year).zfill(4)+str(date.today().month).zfill(2)+str(date.today().day).zfill(2)

# 今天抓到的清單
data_path = join('data', today)
if not os.path.isdir(data_path):
    print(f"資料夾 {data_path} 不存在")
    exit(1)

index_list = [f[:-4] for f in listdir(data_path) if f[-4:] == '.csv']

print(f"今天共有 {len(index_list)} 檔股票")

# 刪除重複的資料並重新排序
for stock_id in index_list:
    rows = []
    file_path = join(data_path, stock_id + '.csv')
    with open(file_path, 'r', encoding='utf-8') as f:
        for row in csv.reader(f, delimiter=','):
            if len(rows) > 0 and row in rows:
                continue
            else:
                rows.append(row)
    
    rows.sort(key=lambda a: a[0])
    
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        cw = csv.writer(f, delimiter=',')
        for row in rows:
            cw.writerow(row)

print("清理完成！")
