

from datetime import datetime

class Person():
    def __init__(self, name, birthyear):
        self._name = name
        self._birthyear = birthyear
        
    def get_birthyear(self):
        return self._birthyear
        
    def set_birthyear(self, v):
        self._birthyear = v
    
    def del_birthyear(self):
        del self._birthyear

    birthyear = property(get_birthyear, set_birthyear, del_birthyear)

p1 = Person('Amy', 2000)
print(p1.get_birthyear())
p1.set_birthyear(2001)
print(p1.get_birthyear())

p2 = Person('Bob', 1980)
print(p2.birthyear)
p2.birthyear = 1981
print(p2.birthyear)

####

class Person():
    def __init__(self, name, birthyear):
        self._name = name
        self._birthyear = birthyear
        
    @property
    def birthyear(self):
        return self._birthyear
        
    @birthyear.setter
    def birthyear(self, v):
        self._birthyear = v
        
    @birthyear.deleter
    def birthyear(self):
        del self._birthyear

p3 = Person('Cathy', 2010)
print(p3.birthyear)
p3.birthyear = 2011
print(p3.birthyear)
