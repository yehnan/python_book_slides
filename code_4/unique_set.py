

li = (3, 1, 'a', 'Amy', 1, 3, 5, 'a')

def unique(iterable):
    result = []
    for x in iterable:
        if x not in result:
            result.append(x)
    return result
    
print(unique(li))
print()

print(set(li))
