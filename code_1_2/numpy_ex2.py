
# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(5)
print("Element's type is", a.dtype)

# 維度
print("Shape is", a.shape)
print()

# 矩陣
from numpy import array, arange

m1 = array([[7, 8, 9], arange(3), [4, 5, 6]])
print("Element's type is", m1.dtype)
print("Shape is", m1.shape)
print(m1)
print()

m2 = array([[1, 2, 3], arange(3), [4, 5, 6]])
print(m2)
print()

m3 = m1 * m2   # not matrix multiplication
print(m3)
print()

m4 = np.dot(m1, m2)  # 3.5 should support @
print(m4)
print()
