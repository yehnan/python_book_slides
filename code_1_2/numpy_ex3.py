
# -*- coding: utf-8 -*-
import numpy as np
import sys

def to_float(x):
    return float(x.strip() or np.nan)
    
# to_float = lambda x: float(x.strip() or np.nan)

fname = 'numpy_ex3_KNMI_20160601_20160630.txt'

avg_temp, min_temp, max_temp = np.loadtxt(fname,  
    delimiter=',', usecols=(2, 3, 4), unpack=True, 
    converters={2: to_float, 3: to_float, 4: to_float}) * 0.1

print('min', min_temp)
print('max', max_temp)
print('avg', avg_temp)
print("# Records", len(min_temp), len(max_temp), len(avg_temp))
print("Minimum", np.nanmin(min_temp))
print("Maximum", np.nanmax(max_temp))
print("Average", np.nanmin(avg_temp))

