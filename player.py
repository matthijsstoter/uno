from dataclasses import dataclass, field

from hand import Hand


@dataclass
class Player:
    name: str
    hand: Hand = field(init=False)

    def __post_init__(self) -> None:
        self.hand = Hand()
    
    @property
    def is_active(self) -> bool:
        if self.hand:
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f"{self.name} with hand {self.hand}"



