"""
Static data for standard 52 cards deck.
"""
UNSPECIFIED_NAME = "Unspecified"
UNSPECIFIED_UNICODE = "❓"

SPADES_DATA = {"name": "Spades", "symbol": "S", "unicode": "♠"}
HEARTS_DATA = {"name": "Hearts", "symbol": "H", "unicode": "♥️"}
CLUBS_DATA = {"name": "Clubs", "symbol": "C", "unicode": "♣️"}
DIAMONDS_DATA = {"name": "Diamonds", "symbol": "D", "unicode": "♦️"}

SUITS_DATA = (SPADES_DATA, HEARTS_DATA, CLUBS_DATA, DIAMONDS_DATA)

TWO_DATA = {"name": "Two", "symbol": "2", "unicode": '2️⃣', "value": 2}
THREE_DATA = {"name": "Three", "symbol": "3", "unicode": '3️⃣', "value": 3}
FOUR_DATA = {"name": "Four", "symbol": "4", "unicode": '4️⃣', "value": 4}
FIVE_DATA = {"name": "Five", "symbol": "5", "unicode": '5️⃣', "value": 5}
SIX_DATA = {"name": "Six", "symbol": "6", "unicode": '6️⃣', "value": 6}
SEVEN_DATA = {"name": "Seven", "symbol": "7", "unicode": '7️⃣', "value": 7}
EIGHT_DATA = {"name": "Eight", "symbol": "8", "unicode": '8️⃣', "value": 8}
NINE_DATA = {"name": "Nine", "symbol": "9", "unicode": '9️⃣', "value": 9}
TEN_DATA = {"name": "Ten", "symbol": "T", "unicode": '🔟🔟🔟🔟🔟🔟', "value": 10}
JACK_DATA = {"name": "Jack", "symbol": "J", "unicode": '💂‍♂️', "value": 11}
QUEEN_DATA = {"name": "Queen", "symbol": "Q", "unicode": '👸', "value": 12}
KING_DATA = {"name": "King", "symbol": "K", "unicode": '👑', "value": 13}
ACE_DATA = {"name": "Ace", "symbol": "A", "unicode": '🅰️', "value": 14}

RANKS_DATA = (TWO_DATA, THREE_DATA, FOUR_DATA, FIVE_DATA, SIX_DATA, SEVEN_DATA, EIGHT_DATA, NINE_DATA, TEN_DATA,
              JACK_DATA, QUEEN_DATA, KING_DATA, ACE_DATA)
