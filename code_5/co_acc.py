


def acc_gf(n):
    while True:
        y = yield n
        n += 1 if y is None else y

acc_g = acc_gf(100)
print(next(acc_g))
print(acc_g.send(3))
print(next(acc_g))
print(acc_g.send(5))

