from dataclasses import dataclass, field

from enum import Enum
from typing import Optional

from itertools import repeat, product


class Colors(Enum):
    RED = "Red"
    BLUE = "Blue"
    YELLOW = "Yellow"
    GREEN = "Green"


class Actions(Enum):
    SKIP = "Skip"
    DRAW4 = "Draw 4 cards"
    DRAW2 = "Draw 2 cards"
    REVERSE = "Reverse"
    WILD = "Wildcard"

class Type(Enum):
    BATTLE = "Battle"
    NORMAL = "Normal"


@dataclass
class Card:
    type: Type
    active: bool = field(init=False, default=True)
    color: Optional[Colors] = None
    value: Optional[int] = None
    action: Optional[Actions] = None

    def __post_init__(self) -> None:
        if self.value is None and self.action is None:
            print("This is an invalid card")

    def __str__(self) -> str:
        if self.value or self.value == 0:
            return f"{self.color.value} {self.value}"
        elif self.action == Actions.DRAW4:
            return f"Draw 4"
        elif self.action == Actions.WILD:
            return f"Wild card"
        elif self.action:
            return f"{self.color.value} {self.action.value}"
        else:
            return "Invalid card"
    
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.active = False
    
    @property
    def is_active(self) -> bool:
        return self.active == True
    
    @property
    def is_inactive(self) -> bool:
        return self.active == False


def create_cards() -> list[Card]:
    CARDS: list[Card] = []
    
    number_cards = [Card(type=Type.NORMAL, color=color, value=i) for color in Colors for i in range(0,10) for _ in range(2)]
    skip_cards = [Card(type=Type.NORMAL, color=color, action=Actions.SKIP) for color in Colors for _ in range(2)]
    draw2_cards = [Card(type=Type.BATTLE, color=color, action=Actions.DRAW2) for color in Colors for _ in range(2)]
    draw4_cards = [Card(type=Type.BATTLE, action=Actions.DRAW4) for _ in range(4)]
    reverse_cards = [Card(type=Type.NORMAL, color=color, action=Actions.REVERSE,) for color in Colors for _ in range(2)]
    wild_cards = [Card(type=Type.NORMAL, action=Actions.WILD) for _ in range(4)]
    CARDS.extend(number_cards)
    CARDS.extend(skip_cards)
    CARDS.extend(draw2_cards)
    CARDS.extend(draw4_cards)
    CARDS.extend(reverse_cards)
    CARDS.extend(wild_cards)
    return CARDS
