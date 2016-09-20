

# Problem 45: Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

from itertools import count
# from itertools import imap as map # 2.x

def tn(n): return n * (n+1) // 2
def pn(n): return n * (3*n - 1) // 2
def hn(n): return n * (2*n - 1)

def filter_equal(ita, itb):
    a = next(ita)
    b = next(itb)
    while True:
        if a < b:
            a = next(ita)
        elif a > b:
            b = next(itb)
        else:
            yield a
            a = next(ita)
            
def tph_gf():
    while True:
        yield from filter_equal(map(hn, count(1)),
                                filter_equal(map(tn, count(1)),
                                             map(pn, count(1))))
        
tph = tph_gf()
print(next(tph))  # 1
print(next(tph))  # 40755
print(next(tph))  # 1533776805
