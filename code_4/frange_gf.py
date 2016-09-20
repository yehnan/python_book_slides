
# -*- coding: utf-8 -*-

def frange(start, end=None, inc=None):
        start = float(start)
        
        if end is None:
            end = start
            start = 0.0
            
        if inc is None:
            inc = 1.0
        
        while abs(start) < abs(end):
            yield start
            start += inc

####


for x in frange(3):
    print(x)
print()
print(list(frange(2.55, 3.7, 0.1)))
print()
print(list(frange(0, 1, 0.1)))

