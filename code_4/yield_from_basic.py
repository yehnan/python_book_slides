

def gf(n):
    for i in range(1, n):
        yield i
    for i in range(-1, -n, -1):
        yield i
        
print(list(gf(5)))

####
def gf2(n):
    yield from range(1, n)
    yield from range(-1, -n, -1)

print(list(gf2(5)))

####

# chain #
def chain(*iterables):
    for itb in iterables:
        yield from itb
        # for e in itb:
            # yield e
            
r = range(5)
li = ['a', 'b', 'c']
t = (0.1, 0.2, 0.3)
for x in chain(r, li, t):
    print(x)

            