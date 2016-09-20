
# -*- coding: utf-8 -*-

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(-18, 18, 36)
noise = 0.1 * np.random.random(len(x))
# 使用sinc，加上一些noise
signal = np.sinc(x) + noise

# interp1d: create linear or cubic  interpolation function
interpolated = interpolate.interp1d(x, signal) # linear
x2 = np.linspace(-18, 18, 36*5) # 5倍
y = interpolated(x2)

cubic = interpolate.interp1d(x, signal, kind="cubic") 
y2 = cubic(x2)

plt.plot(x, signal, 'o', label="data")
plt.plot(x2, y, '-', label="linear")
plt.plot(x2, y2, '--', lw=2, label="cubic")
plt.legend()
#plt.show()
plt.savefig('numpy_ex4.png')
