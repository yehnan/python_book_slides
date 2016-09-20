

# Problem 24: Lexicographic permutations
# https://projecteuler.net/problem=24

#
def perm_gf(s):
    if len(s) == 1:
        yield s[0]
    else:
        for i, c in enumerate(s):
            s_no_i = s[:i] + s[i+1:]
            for sub in perm_gf(s_no_i):
                yield c + sub
                
# for i, x in enumerate(perm_gf('0123456789')):
    # if i < 4:
        # print(x)
    
def lp_perm(s, nth):
    for i, x in enumerate(perm_gf(s)):
        if i == nth:
            return x

####
def factorial(n):
    result = 1
    for i in range(1, n+1):    
        result *= i
    return result
    
def lp(s, nth):
    if nth == 0:
        return s
    else:
        seg = factorial(len(s) - 1)
        idx = nth // seg
        c = s[idx]
        stmp = s[:idx] + s[idx+1:]
        return c + lp(stmp, nth - idx*seg)

#
def test():
    if (list(perm_gf('012')) == ['012', '021', '102', '120', '201', '210'] and
       lp('012', 5 - 1) == '201' and
       lp('0123456789', 10**6 - 1) == lp_perm('0123456789', 10**6 - 1)):
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return lp('0123456789', 10**6 - 1)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

