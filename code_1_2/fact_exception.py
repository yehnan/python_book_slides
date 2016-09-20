
# -*- coding: utf-8 -*-

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
    except TypeError as e:
        print('Error: ' + str(e))
    except ValueError as e:
        print('Error: ' + str(e))
    except (EOFError, KeyboardInterrupt):
        print('\nBye')
        break
    except Exception:
        print('Error: unknown error')
    else:
        print(str(sn) + '! = ' + str(f))
        # print('%s! = %d' % (s, f))

