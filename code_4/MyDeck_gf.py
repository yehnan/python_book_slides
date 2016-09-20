
# -*- coding: utf-8 -*-

def deck_gf():
    cards_count = 52
    suit_count = 13
    suits = ('Spade', 'Heart', 'Diamond', 'Club')
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    
    import random
    li = list(range(cards_count))
    random.shuffle(li)
    cards = tuple(li)
    
    i = 0
    while i < cards_count:
        card_n = cards[i]
        i += 1
        q, r = divmod(card_n, suit_count)
        card = suits[q] + ' ' +  ranks[r]
        yield card

####
deck_g = deck_gf()
print(next(deck_g))
print(next(deck_g))
print(next(deck_g))
print(next(deck_g))
print(next(deck_g))

print('')

for i, card in enumerate(deck_gf()):
    print(i, card)
####

