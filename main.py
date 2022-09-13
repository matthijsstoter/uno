from deck import Deck
from game import Game
from pile import Pile
from rules import Rules
from player_cycle import PlayerCycle
from cli import CLI


def main() -> None:
    deck = Deck()
    pile = Pile()
    cli = CLI()
    cycle = PlayerCycle()
    rules = Rules()
    game = Game(pile=pile, deck=deck, ui=cli, cycle=cycle, rules=rules)
    game.setup_play()
    game.start()
    

if __name__ == "__main__":
    main()

