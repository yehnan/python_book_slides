

import datetime

class Person():
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def say(self, msg='Hello'):
        print(self.name + ' says ' + msg)
    def age(self):
        return datetime.datetime.now().year - self.birthyear

if __name__ == '__main__':
    p = Person('John', 2000)
    print(p.name, p.birthyear)
    p.say()
    p.say('it is so hot')
    print(p.name + ' is ' + str(p.age()) + ' years old.')
    