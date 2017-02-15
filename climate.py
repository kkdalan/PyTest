# -*- coding: utf-8 -*-
# climate.py ( Python 3 version )
import os

def disp_area():
    i = 0 
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i,a[0]), end="")
        i += 1
        if i % 5 == 0: print()

def disp_temp(data):
    print("顯示區域: ", data[0])
    print("----------------------------------")
    for i in range(1,13):
        print("{:>2}月均溫: {:>.1f}度".format(i,float(data[i])))
    print("本季區年均溫為{}度".format(data[13]))
    print("----------------------------------")



target_file = "climate.txt"
with open(target_file,'r',encoding = 'utf-8') as fp:
    raw_data = fp.readlines()

climate_data = []
for item in raw_data:
    area_data = item.rstrip('\n').split()
    climate_data.append(area_data)

while True:
    os.system("clear")
    print("[ 中央氣象局 各地區平居溫度查詢 ]")
    disp_area()
    area = int(input("請輸入您要查詢平均溫度的地區(-1 結束): "))
    if area == -1: break
    disp_temp(climate_data[area])
    x = input("請按Enter 鍵回到主選單")



