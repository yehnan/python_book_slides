
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

def perm_gf(iterable, r=None, p=()):
    items = tuple(iterable) 
    n = len(items)
    r = n if r is None else r
    
    if r == 0:
        yield p
    else:
        for i in range(n):
            yield from perm_gf(items[:i] + items[i+1:], r-1, p+(items[i],))
            # for perm in perm_gf(items[:i] + items[i+1:], r-1, p+(items[i],)):
                # yield perm
    
####
if __name__ == '__main__':
    tests = (list(range(3)), ['a','b','c','d'], list(range(100, 106)))
    for t in tests:
        pa = list(p(t))
        pb = perm(t)
        pc = tuple(perm_gf(t))
        if set(pa) == set(pb) == set(pc):
            print('yes')
        else:
            print('no')
    for t in tests:
        for r in range(1, len(t)):
            pa = list(p(t, r))
            pb = perm(t, r)
            pc = tuple(perm_gf(t, r))
            if set(pa) == set(pb) == set(pc):
                print('yes')
            else:
                print('no')
    