
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open
import csv
import time

filename = 'KNMI_20160101_20160630.txt'

with open(filename, 'r', encoding='utf-8') as fin:
    print('YYYY/MM/DD  %5s %5s %5s' % ('Min', 'MAX', 'AVG'))
    print('-' * 29)
    for line in fin:
        if line.strip()[0] == '#':
            continue
        
        site, date, tavg, tmin, tmax = line.split(',')
        
        date = date.strip()
        year = int(date[:4])
        month = int(date[4:4+2])
        day = int(date[6:])
        
        tavg = float(tavg.strip()) * 0.1
        tmin = float(tmin.strip()) * 0.1
        tmax = float(tmax.strip()) * 0.1
        
        print('%4d/%2d/%2d  %5.1f % 5.1f % 5.1f' % (year, month, day, tmin, tmax, tavg))
        

#### csv

with open(filename, 'r', encoding='utf-8') as fin:
    with open(filename[:-4] + '_new.csv', 'w', encoding='utf-8') as fout:
        csvreader = csv.reader(fin, delimiter=',')
        
        csvwriter = csv.writer(fout, delimiter=',')
        csvwriter.writerow(('YYYY', 'MM', 'DD', 'Min', 'MAX', 'AVG'))
        
        for rows in csvreader:
            if rows[0].strip()[0] == '#':
                continue
                
            site, date, tavg, tmin, tmax = rows
            
            ymd = time.strptime(date, '%Y%m%d') # struct_time
            year = ymd.tm_year
            month = ymd.tm_mon
            day = ymd.tm_mday
            
            tavg = format(float(tavg.strip()) * 0.1, '.1f')
            tmin = format(float(tmin.strip()) * 0.1, '.1f')
            tmax = format(float(tmax.strip()) * 0.1, '.1f')
            
            csvwriter.writerow((year, month, day, tmin, tavg, tmax))

