

def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
        
def fib_r2(n):
    return n if n==0 or n==1 else fib_r(n-1) + fib_r(n-2)
####
def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
####
memo = {0: 0, 1: 1}
def fib_m(n):
    if n not in memo: 
        memo[n] = fib_m(n-1) + fib_m(n-2) 
    return memo[n]

####
def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

####
for x in range(20):
    fr = fib_r(x)
    fi = fib_i(x)
    fm = fib_m(x)
    fr2 = fib_r2(x)

    if fr != fi or fi != fm or fi != fr2:
        print('error: fib(%d) %d %d %d' % (x, fr, fi, fm))


