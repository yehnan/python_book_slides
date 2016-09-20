

class Deck(object):
    pass

d1 = Deck()
print(d1)
Deck.x = 3
d1.y = 4
print(Deck.x, d1.y)

####

print(type(d1), type(Deck))
print(Deck.__name__)
print(d1.__class__)
print(Deck.__bases__)

