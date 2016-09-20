
def bar(): raise ValueError
def foo():
    try:
        bar()
        return 'try'
    except ValueError:
        return 'except'
    else:
        return 'else'
    finally:
        return 'finally'
        
print(foo())
