
# _*_ coding: utf-8 _*_

import json, datetime


with open('earthquake_data.json', 'r') as fin:
    data = json.load(fin)
    
    for item in data['features']:
        print("地點:{}".format(item['properties']['place']))
        print("震度:{}".format(item['properties']['mag']))
        
        # POSIX timestamp, in milliseconds
        ts = float(item['properties']['time']) / 1000.0
        t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("時間:{}".format(t))
        
        print('-' * 20)
        
####

with open('earthquake_data.json', 'r') as fin:
    with open('earthquake_data_new.json', 'w', encoding='utf-8') as fout:
        data = json.load(fin)
        
        data_new = []
        
        for item in data['features']:
            loc = "地點:{}".format(item['properties']['place'])
            mag = "震度:{}".format(item['properties']['mag'])
            
            # POSIX timestamp, in milliseconds
            ts = float(item['properties']['time']) / 1000.0
            t = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            tim = "時間:{}".format(t)
            
            data_new.append((tim, loc, mag))
            
        json.dump(data_new, fout)
            
####

# with open('earthquake_data_new.json', 'r', encoding='utf-8') as fin:
    # data = json.load(fin)
    # for item in data:
        # print(item)
