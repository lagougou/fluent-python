import collections 

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, postion, card):
        assert isinstance(card,Card)
        self._cards[postion] = card

    def __delitem__(self, position):  #inherit MutabelSequence must apply __delitem__ function
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position,value)