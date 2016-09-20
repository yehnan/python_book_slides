

from functools import reduce

# def mul(x, y): return x * y

from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1), 1)
    

