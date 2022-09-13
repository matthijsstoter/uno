from dataclasses import dataclass, field

from card import Card, Colors

# Maybe turn this into a list


@dataclass
class Pile:
    cards: list[Card] = field(init=False, default_factory=list)

    def add(self, card: Card):
        self.cards.append(card)
    
    @property
    def current_card(self) -> Card:
        return self.cards[-1]
    
    @property
    def current_color(self) -> Colors | None:
        return self.current_card.color
    
    @current_color.setter
    def current_color(self, value: Colors) -> None:
        self.current_color = value
    
    def show(self) -> str:
        return str(self.cards[-1])
    
    def reset(self) -> None:
        self.cards = []

    def return_copy(self) -> list[Card]:
        cards = self.cards.copy()
        self.reset()
        return cards
    
    def back_to_deck(self) -> list[Card]:
        cards = self.cards.copy()
        self.cards = [cards[-1]]
        cards.pop()
        return cards

    def __len__(self) -> int:
        return len(self.cards)


x = [1,2,3,4,5]

print(x[:-1])