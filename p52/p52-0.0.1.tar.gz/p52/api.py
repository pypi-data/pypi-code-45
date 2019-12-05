from p52.base import Rank, Suit, Card
from p52.static import *

Spades, Hearts, Clubs, Diamonds = [Suit(**data) for data in SUITS_DATA]
suits = (Spades, Hearts, Clubs, Diamonds)

Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace = [Rank(**data) for data in RANKS_DATA]
ranks = (Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace)


def gen_new_deck():
    cards = list()
    for r in ranks:
        for s in suits:
            cards.append(Card(r, s))
    return cards
