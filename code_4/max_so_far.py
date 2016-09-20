


def max_so_far(m=0):
    def sub(x=m, *t):
        nonlocal m  # 3.x
        x = max(t, default=x)
        if x > m:
            m = x
        return m
    return sub

msf = max_so_far()
print(msf(3))
print(msf(5))
print(msf(-1))
print(msf(6))
print(msf(33))
print(msf(11))
print(msf(67))
print(msf(-1))
