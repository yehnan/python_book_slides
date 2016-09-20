

import random

suits = ('Spade', 'Heart', 'Diamond', 'Club')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

deck = (suits[n//13] + ' ' + ranks[n%13] for n in random.sample(range(52), 52))

for _ in range(5):
    print(next(deck))
print('')

####

deck = (('Spade', 'Heart', 'Diamond', 'Club')[n//13] + ' ' + 
        ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')[n%13] 
        for n in random.sample(range(52), 52))

for _ in range(5):
    print(next(deck))
