from typing import Protocol

from card import Card, Colors
from hand import Hand
from pile import Pile


class UI(Protocol):
    def read_n_players(self) -> int:
        ...

    def read_player_name(self) -> str:
        ...
    
    def read_color(self) -> str:
        ...

    def player_pick_card(self, player_name: str, hand: Hand) -> int:
        ...

    def display_current_card(self, card: Card, current_color: Colors) -> None:
        ...
    
    def top_card(self, pile: Pile) -> Card:
        ...

    def display_rules(self, msg: str) -> None:
        ...

    def cpu_pick_card(self, hand: Hand) -> int:
        ...

    def display_winner(self, winner_name: str) -> None:
        ...
    
    def display_battle_count(self, count: int) -> None:
        ...
    
    def display_start(self, msg: str) -> None:
        ...

    def display_valid_option(self, bo: bool) -> None:
        ...
    
    def buying_cards(self, msg: str) -> None:
        ...
