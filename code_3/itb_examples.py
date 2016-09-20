
####
def product(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

a = range(1, 10+1)
b = [2, 3, 4, 5]
c = [1.1, 3.5, 5.6]
print(product(a, 0.1))
print(product(b))
print(product(c))

####
def my_factorial(n):
    return product(range(2, n+1))

from math import factorial
print('6! is ' + str(my_factorial(6)))
print('math.factorial: ' + str(factorial(6)))
print('10! is ' + str(my_factorial(10)))
print('math.factorial: ' + str(factorial(10)))
print('15! is ' + str(my_factorial(15)))
print('math.factorial: ' + str(factorial(15)))

####
def cumulative_sum(iterable, start=0):
    result = []
    acc = start
    for x in iterable:
        acc += x
        result.append(acc)
    return result


print(cumulative_sum(range(10+1)))
print(cumulative_sum(range(0, 1000, 100)))

#### 
# can be replaced by set
def unique(iterable):
    result = []
    for x in iterable:
        if x not in result:
            result.append(x)
    return result


print(unique([1, 2, 1, 3, 2, 5, 5, 6, 1])) # [1, 2, 3, 5, 6]
print(unique([1, 2, 1, 3, 2, 5])) # [1, 2, 3, 5]
print(unique(range(10)))

####
def duplicate(iterable):
    fst = []
    snd = []
    for x in iterable:
        if x not in fst:
            fst.append(x)
        elif x not in snd:
            snd.append(x)
        else:
            pass
    return snd
        
print(duplicate([1, 2, 6, 1, 3, 2, 5]))
print(duplicate(range(10)))
print(duplicate([1, 1, 3, 1, 3, 3, 1, 2, 1, 5, 2]))

####
def group(iterable, size):
    result = []
    li = list(iterable)
    length = len(li)
    for i in range(0, length, size):
        result.append(li[i:i+size])
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

print(group(range(20), 5))

####
def flatten(iterable):
    result = []
    for x in iterable:
        result.extend(x)
    return result


print(flatten([[0, 1, 2], [3, 4, 5], [6], [7, 8], [9]]))
print(flatten([[0, 1], [3, 5], [6], [7, 8], [9]]))

####






