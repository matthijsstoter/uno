
from typing import Optional

from card import Actions, Card, Colors
from player import Player




class Rules:

    BATTLE_RULES = (
        (Actions.DRAW4, Actions.DRAW4
        ),
        (Actions.DRAW2, Actions.DRAW2
        )
    )

    def check_battle(self, card1: Card, card2: Card) -> bool:
        results = []
        for br in self.BATTLE_RULES:
            # Tuple with actions of the cards
            c = (card1.action, card2.action)

            if c == br:
                print("HOERA")
                results.append(True)
            else:
                results.append(False)
            
        return any(results)


    def check_any_valid_card(self, cards: list[Card], pile_card: Card, current_color: Colors):
        return any([self.check_card(card, pile_card, current_color=current_color) for card in cards])


    def check_card(self, card: Card, pile_card: Card, current_color: Colors
    ) -> bool:

        if card.color == pile_card.color and (pile_card.action is Actions.SKIP 
                                                or pile_card.action is Actions.REVERSE 
                                                or pile_card.action is Actions.DRAW2
                                                ):
            # print("1")
            return True
        
        if (card.color == pile_card.color or card.value == pile_card.value):
            # print("2")
            return True
        
        elif card.value == pile_card.value and pile_card.action is None:
            # print("3")
            return True
        
        elif card.action is pile_card.action and (card.action and pile_card.action):
            print("4")
            return True
        
        elif (card.action == Actions.WILD or card.action == Actions.DRAW4) and pile_card.action is not Actions.DRAW2: 
            # print("5")
            return True
        
        elif ((card.color and card.color == current_color) and (pile_card.action is Actions.WILD or pile_card.action is Actions.DRAW4)):
            return True
        
        elif (card.action is Actions.DRAW2 and pile_card.action is Actions.DRAW2):
            print("YES")
            return True

        # elif (card.action == Actions.WILD)
        
        # elif (card.action == Actions.WILD or card.action == Actions.DRAW4):
        #     if card.color is wild_color:
        #         return True
        #     else:
        #         return False
            
        else:
            return False

    def check_winner(self, players: list[Player]) -> tuple[Player | None, bool]:
        for player in players:
            if not player.is_active:
                return (player, True)
            else:
                return (None, False)

