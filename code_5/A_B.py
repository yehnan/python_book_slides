

class A():
    def __init__(self, x, y):
        self.x = x; self.y = y

class B(A):
    def __init__(self, z):
        super().__init__(0, 0)
        self.z = z
    
b = B(5)
print(b.x, b.y, b.z)

####
