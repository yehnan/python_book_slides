

import random
from concurrent import futures
import time
from multiprocessing import freeze_support
from functools import wraps

# note: changed to use time.perf_counter()
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

@timethis
def foo(data):
    ans = []
    for n in data:
        ans.append(fib(n))
    return ans

@timethis
def bar(data):
    ans = []
    with futures.ProcessPoolExecutor() as pool:
        for fibn in pool.map(fib, data):
            ans.append(fibn)
    return ans

if __name__ == '__main__':
    freeze_support()
    print('Generating data...', end='')
    data = []
    for _ in range(100):
        data.append(random.randint(1, 26))
    print('done\n')
    
    print('Processing data iteratively...')
    foo(data)
    print('done\n')
    
    print('Processing data concurrently...')
    bar(data)
    print('done\n')


    
    
    
    