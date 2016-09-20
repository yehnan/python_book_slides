

# Problem 45: Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

def gen_n(f):
    i = 1
    while True:
        n = f(i)
        yield n
        i += 1

def sub_gf(fa, fb):
    a = next(fa)
    b = next(fb)
    while True:
        if a < b:
            a = next(fa)
        elif a > b:
            b = next(fb)
        else:
            yield a
            a = next(fa)
            
def tph(n):
    tn = gen_n(lambda i: i * (i+1) // 2)
    pn = gen_n(lambda i: i * (3*i - 1) // 2)
    hn = gen_n(lambda i: i * (2*i - 1))

    sub1 = sub_gf(tn, pn)
    sub2 = sub_gf(sub1, hn)
    result = 0
    for i in range(n):
        result = next(sub2)
    return result
    
#
def test():
    if tph(1) == 1 and tph(2) == 40755:
        return 'Pass'
    else:
        return 'Fail'

def main():
    return tph(3)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

