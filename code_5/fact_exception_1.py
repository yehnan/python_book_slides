
# -*- coding: utf-8 -*-

# int()與fact()都會引發ValueError

def fact(n):
    if n < 0:
        raise ValueError('Argument must be non-negative')
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

while True:
    try:
        s = input('input n: ')
        sn = int(s)
        f = fact(sn)
    except ValueError as e:
        print('Error: ' + str(e))
    except (EOFError, KeyboardInterrupt):
        print('\nBye')
        break
    except Exception as e:
        print('Unknown Error: ' + str(e))
    else:
        print(str(sn) + '! = ' + str(f))

