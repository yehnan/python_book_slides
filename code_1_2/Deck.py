

import random
# from collections import abc

# class Deck(abc.Sized, object):
class Deck(object):
    cards_count = 52
    
    # spade, heart, diamond, club
    suits = ('Spade', 'Heart', 'Diamond', 'Club')
    suits_shortname = 'SHDC'
    suit_count = 13
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    
    def __init__(self):
        # 0~12  are Spade A~K,
        # 13~25 are Heart A~K,
        # 26~38 are Diamond A~K,
        # 39~51 are Club A~K
        # True means not-drawed-yet
        self.cards = list(range(Deck.cards_count))
        # print(self.cards)
        
    def draw(self):
        card = ''
        if len(self.cards) > 0:
            i = random.randrange(len(self.cards))
            card_n = self.cards.pop(i)
            q, r = divmod(card_n, Deck.suit_count)
            # print(card_n, q, r)
            card = ' '.join((Deck.suits[q], Deck.ranks[r]))
            
        return card
    
    def __iter__(self):
        return self
        
    def __next__(self):
        card = self.draw()
        if card != '':
            return card
        else:
            raise StopIteration('Deck is empty')
        
    # def next(self):
        # return self.__next__()
    
    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return 'The deck remains %d cards.' % len(self.cards)
        
if __name__ == '__main__':
    d = Deck()
    print(len(d))
    for _ in range(5):
        print(d.draw())
    print(len(d))
    
    d2 = Deck()
    print(d2)
    d2.draw()
    print(d2)
    for card in d2:
        print(card)

    # print(next(d2))
    # print(next(d2))
    # print(d2)
    # print(issubclass(Deck, abc.Sized))
    
    
    