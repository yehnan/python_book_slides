

b = 5
def foo():
    a = b + 5
    return a
def bar():
    b = 2
    return foo()
    
print(foo())
print(bar())
