import json
from collections import defaultdict
import os, io
# d = defaultdict(list)
# d['points'].append('(160,171), (204,171), (204,188), (160,188)')
# d['points'].append('(160,171), (204,171), (204,188), (160,188)')
# print(d)
# json_str = json.dumps(d)
# print(json_str)
# lines = d["points"]
# print(lines)
# for items in lines:
#     print(items)
# with open('./1.json','w') as f:
#     f.write(json_str)

with open('D:/大四下/中国软件杯/Bank_Card_OCR/数据标注程序/annotation/annotation.txt','r') as f:
    lines = f.readlines()
for line in lines:
    item = line.split("(",)
    # print(item[1][:-3])
    # print(item[2][:-3])
    # print(item[3][:-3])
    # print(item[4][:-12])
    d = defaultdict(list)
    d[''].append(item[1][:-3] + ','+ item[2][:-3]+',' + item[3][:-3] + ',' + item[4][:-12])
    json_str = json.dumps(d)
    print(json_str)
    print(line[:6])
    #d['points'].append('(160,171), (204,171), (204,188), (160,188)')
    with open('./'+line[:6]+'.json', 'a') as f:
        f.write(json_str+'\n')

