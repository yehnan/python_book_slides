

def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

####

class Fibmemo():
    def __init__(self):
        self.memo = {0: 0, 1: 1}
    
    def __call__(self, n):
        if n not in self.memo: 
            self.memo[n] = self(n-1) + self(n-2) 
        return self.memo[n]

fib = Fibmemo()
print(fib(3), fib(5), fib(7))


#### context management protocol
print()

class Fib():
    def __init__(self):
        self.memo = {0: 0, 1: 1}
    
    def __call__(self, n):
        if n not in self.memo: 
            self.memo[n] = self(n-1) + self(n-2) 
        return self.memo[n]
    
    def __enter__(self):
        self.memo = {0: 0, 1: 1}
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.memo = {0: 0, 1: 1}
        return False # don't supress the exception

with Fib() as fib:
    for n in range(1, 9+1):
        print('fib(%2d) = %4d, memo len is %2d' % (n, fib(n), len(fib.memo)))
print(len(fib.memo))

with Fib() as fib:
    for n in range(1, 20+1):
        print('fib(%2d) = %4d, memo len is %2d' % (n, fib(n), len(fib.memo)))
print(len(fib.memo))
