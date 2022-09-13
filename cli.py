import random

from card import Card, Colors
from hand import Hand
from pile import Pile


class CLI:
    def read_n_players(self) -> int:

        # while True:
        #     n = input("How many players are playing?")

        #     try:
        #         n_players = int(n)
        #         return n_players
        #     except ValueError:
        #         Raise("Please provide a number")
        
        return 3

    def read_player_name(self) -> str:
        return "Name"
        # return input("What's your player name?")
    
    def read_color(self) -> str:
        colors_string = ", ".join(
        f"{color.name}" for _, color in enumerate(Colors))
        print(f"Please select a color: {colors_string}")

        while True:
            try:
                print(f"Pick a card color!")
                choice = input()
                if choice in colors_string:
                    return choice
                print("Please select a valid color")
            except TypeError:
                "That's not a number! :("

    def player_pick_card(self, player_name: str, hand: Hand) -> int:
        while True:
            try:
                print(f"{player_name}! Pick a card {hand.show()}")
                choice = int(input())
                if 0 <= choice < len(hand.cards) + 1:
                    return choice
                elif choice == -1:
                    return choice
                print("Please select a valid card number")
            except ValueError:
                "That's not a number! :("

    def display_current_card(self, card: Card, current_color: Colors) -> None:
        print(f"The current card is a {card}")
        if not card.color:
            try:
                print(f"The current color is {current_color.value}")
            except AttributeError:
                print(f"The current color is {card.color}")
    
    def top_card(self, pile: Pile) -> Card:
        return pile.current_card

    def display_rules(self) -> None:
        print("########################")
        print("\n \n")

        print("Please don't cheat")
        print("To draw a card, pick -1")
        print("\n \n")

        print("########################")

    
    def cpu_pick_card(self, hand: Hand) -> int:
        n_cards = len(hand)
        return random.randint(0, n_cards-1)


    def display_winner(self, winner_name: str) -> None:
        print(f"{winner_name} won the game! :)")
