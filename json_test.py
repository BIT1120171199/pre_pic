import json, io
from collections import defaultdict
filename = 'C:/Users/Burning/Desktop/数据集/json/0001.json'
with io.open(filename, 'r', encoding='utf-8') as f:
    data = f.readlines()
for d1 in data:
    print(d1)
    print(d1[7:].split(',')[0])
    print(d1[7:].split(',')[1])
    print(d1[7:].split(',')[2])
    print(d1[7:].split(',')[3])
    print(d1[7:].split(',')[4])
    print(d1[7:].split(',')[5])
    print(d1[7:].split(',')[6])
    print(d1[7:].split(',')[7][:-4])
d = defaultdict(list)
d[''].append(d1[7:].split(',')[0] + ',' + d1[7:].split(',')[1] + ',' + d1[7:].split(',')[2] + ','
             + d1[7:].split(',')[3] + ',' + d1[7:].split(',')[4] + ',' + d1[7:].split(',')[5]
             + ',' + d1[7:].split(',')[6] + ',' + d1[7:].split(',')[7][:-4])
json_str = json.dumps(d)
print(json_str)
#d['points'].append('(160,171), (204,171), (204,188), (160,188)')
with open('./'+str(1000)+'.json', 'a') as f:
    f.write(json_str+'\n')

