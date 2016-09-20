
# -*- coding: utf-8 -*-

# class CustomError(Exception):
    # def __init__(self, message, status):
        # super().__init__(message, status)
        # self.message = message
        # self.status = status
        
class NegativeIntError(ValueError):
    pass
    
def fact(s):
    n = int(s, 0)
    if n < 0:
        raise NegativeIntError('Argument must be non-negative')
        
    result = 1
    for i in range(1, n+1): 
        result *= i
    return (n, result)

while True:
    try:
        s = input('input n: ')
        n, f = fact(s)
    except NegativeIntError as e:
        print('Error: ' + str(e))
    except ValueError as e:
        print('Error: can not convert %s to integer' % s)
    except (EOFError, KeyboardInterrupt):
        print('\nBye')
        break
    except Exception as e:
        print('Unknown Error: ' + str(e))
    else:
        print(str(n) + '! = ' + str(f))

