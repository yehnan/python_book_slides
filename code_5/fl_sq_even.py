
# -*- coding: utf-8 -*-

def sq(n): return n**2
def even(n): return n%2 == 0

def sq_even(n):
    return map(sq, filter(even, range(1, n)))

# 1到10中的偶數平方，相加後的總和    
print(sum(sq_even(10)))

# 使用sum
def sum_sq_even(n):
    return sum(
               map(sq, 
                   filter(even, 
                       range(1, n))))
print(sum_sq_even(10))

# 使用reduce
from functools import reduce
from operator import add
def sum_sq_even(n):
    return reduce(add,
               map(sq, 
                   filter(even, 
                       range(1, n))))
                       
print(sum_sq_even(10))

# 使用產生器運算式
print(sum(n**2 for n in range(1, 10) if n%2 == 0))

