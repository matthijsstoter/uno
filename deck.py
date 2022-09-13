from dataclasses import dataclass, field
import random

from card import Card, create_cards


@dataclass
class Deck:
    cards: list[Card] = field(init=False, default_factory=list)

    def __post_init__(self) -> None:
        self.cards = create_cards()
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()
    
    def deal(self, n: int) -> list[Card]:
        cards = self.cards[-n:]
        del self.cards[-n:]
        return cards
    
    def show(self) -> str:
        return ", ".join(
        f"({card})" for card in self.cards
        )

    def __len__(self) -> int:
        return len(self.cards)
    
    def reset(self, cards: list[Card]) -> None:
        self.cards = cards
        self.shuffle()

