import random
from datetime import datetime

from p52.api import gen_new_deck


class Deck:
    """
    52 cards Deck implementation
    """
    __cards = list()
    trump = None

    def __init__(self,
                 init_shuffle=True,
                 *args, **kwargs):
        self.__cards = gen_new_deck()

        self.shuffle() if init_shuffle else None
        self.time = datetime.now()
        self.__name__ = f"Deck {hex(self.__hash__())}"
        self.__repr__ = f"{self.__name__}\n" \
                        f"Created: {self.time}\n" \
                        f"Cards: {self.number_of_cards}\n"

    def __iter__(self):
        for card in self.__cards:
            yield card

    def __len__(self):
        return len(self.__cards)

    def __repr__(self):
        return self.__repr__

    def __str__(self):
        return self.__name__

    def __hash__(self):
        return hash(self.time)

    def __getitem__(self, item):
        return self.__cards[item]

    @property
    def number_of_cards(self):
        return self.__len__()

    def get_cards(self):
        return self.__cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def fetch_card(self):
        return self.__cards.pop()
