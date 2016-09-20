

def fact(n):
    if type(n) is not int:
        return -2
    if n < 0:
        return -1

    result = 1
    for i in range(1, n+1):
        result *= i
    return result

while True:
    s = input('input n: ')
    n = int(s)       #
    ans = fact(n)
    if ans == -2:
        print('Must input integer')
    elif ans == -1:
        print('Must be non-negative')
    else:
        print('%d! = %d' % (n, ans))
