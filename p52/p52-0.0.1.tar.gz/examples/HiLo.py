"""
Simple game for one player. If rank of the card you fetch is bigger than PC's card, you win.
"""
from p52.deck import Deck


if __name__ == '__main__':
    while 1:
        try:
            d = Deck()
            d.shuffle()
            you_card = d.fetch_card()
            print(f"Your card is {you_card}")
            pc_card = d.fetch_card()
            print(f"pc card is {pc_card}")
            if you_card > pc_card:
                print("You win")
            elif you_card < pc_card:
                print("You lose")
            else:
                print("Equal")
            input("Press enter to continue or ctrl+c to quit...")
        except KeyboardInterrupt:
            break
