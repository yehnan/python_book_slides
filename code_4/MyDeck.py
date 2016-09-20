

try: 
    input = raw_input
except NameError:
    pass

import random

class MyDeckIterator(object):
    def __init__(self, deck):
        self.deck = deck
        self.i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        try:
            card = self.deck[self.i]
            self.i += 1
            return card
        except IndexError:
            raise StopIteration('No more card') 
    def next(self):
        return self.__next__()

class MyDeck(object):
    cards_count = 52
    
    # spade, heart, diamond, club
    suits = ('Spade', 'Heart', 'Diamond', 'Club')
    suit_count = 13
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    
    def __init__(self):
        # 0~12  are Spade A~K,
        # 13~25 are Heart A~K,
        # 26~38 are Diamond A~K,
        # 39~51 are Club A~K
        # True means not-drawed-yet
        li = list(range(MyDeck.cards_count))
        random.shuffle(li)
        
        self.cards = tuple(li)
        
    def __getitem__(self, i):
        if 0 <= i < MyDeck.cards_count:
            card_n = self.cards[i]
            q, r = divmod(card_n, MyDeck.suit_count)
            
            card = MyDeck.suits[q] + ' ' +  MyDeck.ranks[r]
            return card
        else:
            raise IndexError('Index out of range')
        
    def __iter__(self):
        return MyDeckIterator(self)
        
    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return 'The deck remains %d cards.' % len(self.cards)

        
####

if __name__ == '__main__':
    d1 = MyDeck()
    # for i in range(MyDeck.cards_count):
        # print(d1[i])
    # print(len(d1))
    # print(len(d1))
    
    # for card in d1:
        # print(card)
    # input('Press Entery to continue...')
    # for card in d1:
        # print(card)
    # input('Press Entery to continue...')
    
    # ditr_1 = iter(d1)
    # ditr_2 = iter(d1)
    
    # print('-' * 20)
    # print('ditr_1 ' + next(ditr_1))
    # print('ditr_1 ' + next(ditr_1))
    # print('                    ditr_2 ' + next(ditr_2))
    # print('ditr_1 ' + next(ditr_1))
    # print('                    ditr_2 ' + next(ditr_2))
    # print('ditr_1 ' + next(ditr_1))
    # print('ditr_1 ' + next(ditr_1))
    # print('                    ditr_2 ' + next(ditr_2))
    # print('ditr_1 ' + next(ditr_1))
    # print('                    ditr_2 ' + next(ditr_2))
    # print('-' * 20)
    
    # input('Press Entery to stop')

