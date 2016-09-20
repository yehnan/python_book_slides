
# -*- coding: utf-8 -*-
from itertools import permutations
p = permutations

def perm(iterable, r=None):
    items = tuple(iterable) # 欲排列的東西
    r = len(items) if r is None else r
    
    answers = [] # 存放結果的串列
    
    def sub(items, k, p): # 從items裡取出k個，p是目前已有的排列
        if k == 0:
            answers.append(p)
        else:
            for i in range(len(items)):
                # 遞迴呼叫，去掉索引i的元素
                sub(items[:i] + items[i+1:], k-1, p+(items[i],))
    sub(items, r, ())
    
    return answers
    
####
from itertools import product

# print(tuple(product(range(3), repeat=3)))

def perm_product(iterable, r=None):
    items = tuple(iterable)
    n = len(items)
    r = n if r is None else r
    
    answers = []
    
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            answers.append(tuple(items[i] for i in indices))
            
    return answers
    
####

def perm_product_gf(iterable, r=None):
    items = tuple(iterable)
    n = len(items)
    r = n if r is None else r
    
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(items[i] for i in indices)
            
####
if __name__ == '__main__':
    tests = (list(range(3)), ['a','b','c','d'], list(range(100, 106)))
    for t in tests:
        pa = list(p(t))
        pb = perm(t)
        pc = perm_product(t)
        pd = tuple(perm_product_gf(t))
        if set(pa) == set(pb) == set(pc) == set(pd):
            print('yes')
        else:
            print('no')
    for t in tests:
        for r in range(1, len(t)):
            pa = list(p(t, r))
            pb = perm(t, r)
            pc = perm_product(t, r)
            pd = tuple(perm_product_gf(t, r))
            if set(pa) == set(pb) == set(pc) == set(pd):
                print('yes')
            else:
                print('no')
    