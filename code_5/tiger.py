

class MyClass():
    def __init__(self): self.x = 3
    def foo(self):
        self.x += 1;   print(self.x)
    def bar(tiger, n):
        tiger.x += n;  print(tiger.x)

c = MyClass()
c.foo()           # ?
MyClass.foo(c)    # ?
c.bar(-2)         # ?
MyClass.bar()     # ?
c.foo(c)          # ?
