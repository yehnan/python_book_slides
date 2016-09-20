


def counter_shared(n):
    def inc(x):
        nonlocal n
        n += x
        return n
        
    def dec(x):
        nonlocal n
        n -= x
        return n
        
    return inc, dec
    
c_inc, c_dec = counter_shared(60)
print(c_inc(1)) # 61
print(c_inc(4)) # 65
print(c_dec(2)) # 63
print(c_inc(5)) # 68
print(c_dec(2)) # 66


