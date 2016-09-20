

def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()
        res = func(*args, **kwargs)
        t_end = time.clock()
        print(func.__name__, t_end-t_start)
        return res
    return wrapper

####

def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

####
@dec_time
def fib_i_test(n):
    for i in range(n):
        fib_i(i)

@dec_time
def fib_m_test(n):
    for i in range(n):
        fib_m(i)
        
fib_i_test(5000)
fib_m_test(5000)

