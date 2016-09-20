


class Person():
    HI_STR = 'Hi, I am '

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print('Hello, I am ' + self.name)
        
    def say_hi(self):    
        print(Person.HI_STR + self.name)



p1 = Person('Amy', 25)
p2 = Person('Bob', 38)
p1.say_hello()
Person.say_hello(p1)
p2.say_hello()

p1.say_hi()
p2.say_hi()

