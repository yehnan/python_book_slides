
# -*- coding: utf-8 -*-

def fact(n):
    if n < 0:
        raise ValueError('Argument must be non-negative')
        
    result = 1
    for i in range(1, n+1): 
        result *= i
    return (n, result)

while True:
    try:
        try:
            s = input('input n: ')
            if len(s) == 0:
                continue
            sn = int(s)
        except ValueError as e:
            print('Error: can not convert %s to integer' % s)
            continue
            
        n, f = fact(sn)
    except ValueError as e:
        print('Error: %s' % str(e))
    except (EOFError, KeyboardInterrupt):
        print('\nBye')
        break
    except Exception as e:
        print('Unknown Error: ' + str(e))
    else:
        print(str(n) + '! = ' + str(f))

