

class A():
    def __init__(self):
        self.x = 3
        self.__pi = 3.14
    def foo(self):
        print(self.__pi)
        
class B(A):
    def __init__(self):
        super().__init__()
        self.z = self.x + 100

    def bar(self):
        # return self.__pi # error
        return self._A__pi # ok
a = A()
b = B()
print(b.x,b.z)
# print(a.__pi) # error
a.foo()
print(b.bar())

