
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open

f1 = 'file_basic.txt'
f2 = 'file_basic_utf8.txt'
f3 = 'file_basic_big5_cp950.txt'

fin = open(f1, 'r')
# fin = open(f3, 'r', encoding='big5') # ascii  big5  cp950  utf-8

for line in fin:
    print(line, end='')
    
fin.close()

#### 

# print()

# with open('file_basic.txt', 'r') as fin:
    # for line in fin:
        # print(line, end='')
        
        
        
