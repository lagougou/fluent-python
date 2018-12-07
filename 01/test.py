from frenchdeck import FrenchDeck,Card
from vector import Vector

beer_card = Card('7','diamond')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[1])

print(deck[:5])



suit_values = dict(spades=3,hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card  in sorted(deck,key=spades_high):
    print(card)

Vector(2,4)

print(deck._cards)
print(deck[12::13])