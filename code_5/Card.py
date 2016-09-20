

class Card():
    suits = {'spade': 4, 'heart': 3,
             'diamond': 2, 'club': 1}
    ranks = {'A': 14, '2': 15, '3': 3,
             '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9,
             '10': 10, 'J': 11, 'Q': 12, 'K': 13}
             
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other):
        rank_diff = Card.ranks[self.rank] - Card.ranks[other.rank]
        if rank_diff < 0:
            return True
        elif rank_diff == 0:
            if Card.ranks[self.rank] < Card.ranks[other.rank]:
                return True
            
        return False
        
c1 = Card('spade', 'A')
c2 = Card('spade', 'K')
c3 = Card('heart', '9')
c4 = Card('club', '2')
print(c1 < c2)
print(c2 < c3)
print(c3 < c4)
print(c4 < c1)
