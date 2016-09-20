


def unique(iterable, key=lambda x: x):
    seen = set()
    
    for elem, ekey in ((x, key(x)) for x in iterable):
        if ekey not in seen:
            yield elem
            seen.add(ekey)


t = (1, 2, 5, 6, 7, 1, 2, 3, 6, 4, 3, 1, 2, 6)
ug = unique(t)
for x in ug:
    print(x)


