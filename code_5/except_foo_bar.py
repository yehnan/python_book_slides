


def foo():
    try:
        raise ValueError
    except IndexError:
        print('foo IndexError')
    else:
        print('foo else')
    finally:
        print('foo finally')
    print('foo end')
    
def bar():
    try:
        foo()
    except ValueError:
        print('bar ValueError')
    else:
        print('bar else')
    finally:
        print('bar finally')
    print('bar end')
    
bar()  # what will be printed?
