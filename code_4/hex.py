
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open
import sys

HEX = 16
template = '%02X ' * HEX
template_head = '      ' + template
# template_line = '%02X  ' + template

def hex_show(filename, max=None):
    with open(filename, 'rb') as fin:
        print(template_head % tuple(range(HEX)))
        print()
        
        data = fin.read(HEX)
        len_total = 0
        while len(data):
            len_total += len(data)
            if max and len_total > max:
                break
                
            head = (len_total // HEX - (1 if len_total % HEX == 0 else 0)) * HEX
            print('%04X  ' % head, end='')
            for b in data:
                print('%02X ' % b, end='')
            print()
            
            data = fin.read(HEX)

if len(sys.argv) == 2:
    hex_show(sys.argv[1], HEX*8)
elif len(sys.argv) == 3:
    hex_show(sys.argv[1], None if int(sys.argv[2]) <= 0 else int(sys.argv[2]))
else:
    print('Usage: hex.py <filename>')


