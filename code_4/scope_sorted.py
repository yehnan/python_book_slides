

# sorted(iterable[, key][, reverse])

t = (('Bob', 180, 80), ('Amy', 160, 60), ('Cathy', 170, 50))

NAME_I, HEIGHT_I, WEIGHT_I = range(3)

def k_height(item):
    return item[HEIGHT_I]
    
# def k_weight(item):
    # return item[WEIGHT_I]

# print(sorted(t, key=k_height))
# print()

def foo(data):
    HEIGHT_I = 99
    return sorted(data, key=k_height)

print(foo(t))



####
print()

print(sorted(t, key=lambda x: x[0])) # name
print(sorted(t, key=lambda x: x[1])) # height
print(sorted(t, key=lambda x: x[2])) # weight
print()


####
def sorted_by(data, what='name', reverse=False):
    d = {'name': 0, 'height': 1, 'weight': 2}
    i = d.get(what, 0)
    
    return sorted(data, key=lambda x: x[i], reverse=reverse)

print(sorted_by(t, 'name'))
print(sorted_by(t, 'height', reverse=True))
print(sorted_by(t, what='weight'))
print(sorted_by(t, reverse=True))
