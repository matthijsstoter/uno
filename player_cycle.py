from player import Player


class PlayerCycle():
    def __init__(self):
        self.players: list[Player] = []
        self._pos: int = -1
        self.reverse: bool = False
    
    def __next__(self) -> Player:
        self.pos = self.pos + self.step
        return self.players[self.pos]
    
    def __len__(self) -> int:
        return len(self.players)

    @property
    def step(self) -> int:
        if self.reverse:
            return -1
        else:
            return 1
    
    @property
    def pos(self) -> int:
        return self._pos
    
    @pos.setter
    def pos(self, value):
        self._pos = value % len(self.players)
    
    def reverse_dir(self) -> None:
        if self.reverse:
            self.reverse = False
        else:
            self.reverse = True
    
    def add_player(self, player: Player) -> None:
        self.players.append(player)
    
    def remove_player(self, player: Player) -> None:
        self.players.remove(player)