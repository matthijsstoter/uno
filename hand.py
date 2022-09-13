from dataclasses import dataclass, field

from card import Card


@dataclass
class Hand:
    cards: list[Card] = field(init=False, default_factory=list)

    def __str__(self) -> str:
        cards = [str(f) for f in self.cards]
        return ", ".join(cards)

    def set(self, cards: list[Card]) -> None:
        self.cards = cards
    
    def pick_a_card(self, index) -> Card:
        return self.cards.pop(index)
    
    def draw_a_card(self, card: Card, n: int = 1) -> None:
        for _ in range(n):
            self.cards.append(card)
    
    def show(self) -> str:
        return ", ".join(
        f"({index} for {card})" for index, card in enumerate(self.cards)
    )

    def see_card(self, index) -> Card:
        return self.cards[index]

    def __len__(self) -> int:
        return len(self.cards)
