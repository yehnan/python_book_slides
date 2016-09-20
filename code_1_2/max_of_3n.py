
# -*- coding: utf-8 -*-
import random

def max_of_3n(a, b, c):
    x = None
    if a < b:        # 縮排零層
        if b < c:        # 縮排一層
            x = c            # 縮排二層
        else:            # 縮排一層
            x = b            # 縮排二層
    else:            # 縮排零層
        if a < c:        # 縮排一層
            x = c            # 縮排二層
        else:            # 縮排一層
            x = a            # 縮排二層
    # 最後x會是a、b、c中最大的
    return x

def max_of_3n_b(a, b, c):
    return (c if b < c else b) if a < b else (c if a < c else a)

if __name__ == '__main__':
    for _ in range(100):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        m1 = max(a, b, c)
        m2 = max_of_3n(a, b, c)
        m3 = max_of_3n_b(a, b, c)
        if m1 != m2:
            print('fail', a, b, c, m1, m2)
        if m1 != m3:
            print('fail', a, b, c, m1, m3)
