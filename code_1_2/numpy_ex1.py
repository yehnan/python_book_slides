

import numpy as np

# Python's list and *
print([1, 2, 3, 4] * 3)
print()

# numpy's array and *
print(np.arange(5))
print(np.arange(5) * 3)
print()

def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

print(numpysum(5))


   