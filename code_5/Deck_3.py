
import random

class Deck(object):
    cards_count = 52
    suits = ('Spade', 'Heart', 'Diamond', 'Club')
    suit_count = 13
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):
        li = list(range(Deck.cards_count))
        random.shuffle(li)
        
        self.cards = tuple(li)
        
    # def __getitem__(self, i):
    def draw(self, i):
        if 0 <= i < Deck.cards_count:
            card_n = self.cards[i]
            q, r = divmod(card_n, Deck.suit_count)
            card = Deck.suits[q] + ' ' +  Deck.ranks[r]
            return card
        else:
            raise IndexError('Index out of range')

d1 = Deck()
d2 = Deck()
print('%10s   %10s' % ('d1', 'd2'))
for i in range(5):
    print('%10s   %10s' % (d1.draw(i), d2.draw(i)))
