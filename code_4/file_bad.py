
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open

f1 = 'file_basic.txt'
f2 = 'file_basic_utf8.txt'
f3 = 'file_basic_big5_cp950.txt'

with open('file_basic.txt', 'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        print(line, end='')
        
        
with open('file_basic.txt', 'r', encoding='utf-8') as fin:
    line = fin.readline()
    while line:
        print(line, end='')
        line = fin.readline()
