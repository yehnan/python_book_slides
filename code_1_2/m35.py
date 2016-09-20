

# Problem 1: Multiples of 3 and 5
# https://projecteuler.net/problem=1

#
def m35_a(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

#
def m35_b(n):
    return sum(i for i in range(1, n) if i%3 == 0 or i%5 == 0)

#
def m35_c(n):
    sm3 = sum(range(3, n, 3))
    sm5 = sum(range(5, n, 5))
    sm15 = sum(range(3*5, n, 3*5))
    return sm3 + sm5 - sm15

#
def m35_d(n):
    def sub(n):
        a, b = 3, 5
        while a < n or b < n:
            if a < b:
                yield a
                a += 3
            elif a == b:
                yield a
                a += 3
                b += 5
            elif a > b:
                yield b
                b += 5
    return sum(sub(n))

#
def m35_e(n):
    from operator import add
    from functools import reduce
    def is_m35(n):
        return n%3 == 0 or n%5 == 0
    return reduce(add, filter(is_m35, range(1, n)), 0)

#
def test():
    m35all = [m35_a, m35_b, m35_c, m35_d, m35_e]
    n = 10
    for f in m35all:
        if f(n) != 23:
            return 'Fail'
            break
    #
    n = 1000
    a = m35_a(n)
    b = m35_b(n)
    c = m35_c(n)
    d = m35_d(n)
    e = m35_e(n)
    if a == b == c == d == e:
        return 'Pass'
    else:
        return 'Fail'

def main():
    return m35_a(1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

