


class Person():
    HI_STR = 'Hi, I am '

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print('Hello, I am ' + self.name)
        
    def say_hi(self):    
        print(Person.HI_STR + self.name)

    def __str__(self):
        return '<Person> %s, age %d' % (self.name, self.age)

    def __repr__(self):
        return "Person('%s', %d)" % (self.name, self.age)
        
p1 = Person('Amy', 25)
p2 = Person('Bob', 38)
p1.say_hello()
Person.say_hello(p1)
p2.say_hello()

p1.say_hi()
p2.say_hi()

print(p1)
print(str(p2), p2.__str__())
print(repr(p1), p1.__repr__())

print()
exec('p3 = ' + repr(p2))
print(p3)
print(p3.name, p3.age)
