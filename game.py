from dataclasses import dataclass, field
import os

from card import Actions, Card, Colors, Type
from ui import UI
from deck import Deck
from pile import Pile
from rules import Rules
from player import Player
from player_cycle import PlayerCycle


@dataclass
class Game:
    cycle: PlayerCycle
    deck: Deck
    pile: Pile
    ui: UI
    rules: Rules
    n_cards: int = 7
    _current_player: Player = field(init=False, repr=False)
    _battle: bool = field(init=False, repr=False, default=False)
    _battle_count: int = field(init=False, repr=False, default=0)
    _color_status: bool = field(init=False, repr=False, default=True)
    _current_color: Colors = field(init=False, repr=False)

    @property
    def current_color(self) -> Colors | None:
        """Color of top card on pile"""
        return self.pile.current_color

    @property
    def players(self) -> list[Player]:
        """List of players"""
        return self.cycle.players
    
    @property
    def n_players(self) -> int:
        """Number of players"""
        return len(self.cycle.players)
    
    @property
    def rounds(self) -> int:
        return self.cycle.pos

    def setup_play(self) -> None:
        """Read number of player and player names. """          

        # n_players = self.cli.read_n_players()
        # for _ in range(n_players):
            # self.cycle.add_player(Player(name=self.cli.read_player_name()))

        # Development number of players and add_player to cycle
        names = ["Matthijs", "Denise", "Jesper"]
        
        for name in names:
            self.cycle.add_player(Player(name=name))

    def start(self) -> None:
        """Start the game"""
        print(f"Handing out cards to {len(self.players)} players.\n")
        self.hand_out_cards()

        self.ui.display_rules()

        print(f"Drawing the first card, is everybody ready?\n")
        self.pile.add(self.deck.draw())
        self.check_first_card()
        self._current_color = self.pile.current_card.color

        playing = True

        while playing:
            self.do_turn()

    def do_turn(self) -> None:
        
        print("Checking for winner")
        self.check_winner()
        self.check_deck()

        self._current_player = next(self.cycle)
        self.do_player_turn(self._current_player)
    
    def do_turn_shell(self) -> None:
        self.do_player_turn(self._current_player)
    
    def do_player_turn(self, player: Player) -> None:
        pile_card = self.pile.current_card
        
        self.ui.display_current_card(pile_card, current_color=self._current_color)

        valid_option = self.rules.check_any_valid_card(player.hand.cards, pile_card, current_color=self._current_color)
        # print(f"\n \n \n Can {player.name} play a card? {check_any_valid_card(player.hand.cards, pile_card, wild_color=None)} \n \n \n")

        i = self.ui.player_pick_card(player.name, player.hand)

        if i >= 0:
            card = player.hand.see_card(i)

            # Check if the current card is a battle card
            if self.check_battle_card(card=pile_card):

                # Check if the battle is active
                if self._battle:
                    if self.check_valid_battle_card(player_card=card, pile_card=pile_card):
                        player.hand.pick_a_card(index=i)
                        self.pile.add(card)
                    else:
                        self.do_turn_shell()        
                        
            if self.rules.check_card(card=card, pile_card=pile_card, current_color=self._current_color):
                player.hand.pick_a_card(index=i)
                self.pile.add(card=card)

                if self.check_battle_card(card=card):
                    self._battle = True
                
                if self.check_wild(card=card):
                    self._color_status = False
                    
                if self.check_draw4(card=card):
                    self._color_status = False
                

            else:
                self.do_turn_shell()
        
            # os.system("clear")

        
        elif i == -1:
            # os.system("clear")
            if self.check_battle() and self._battle:
                if pile_card.action is Actions.DRAW4:
                    print(self._buy_x_cards(player_name=player.name, number=4, n_cards=self._battle_count))
                    for _ in range(self._battle_count):
                        player.hand.draw_a_card(self.deck.draw(), 4)
                
                elif pile_card.action is Actions.DRAW2:
                    print(self._buy_x_cards(player_name=player.name, number=2, n_cards=self._battle_count))
                    for _ in range(self._battle_count):
                        player.hand.draw_a_card(self.deck.draw(), 2)
                
                self._battle = False
                self.pile.current_card.deactivate()
            
            else:
                player.hand.draw_a_card(self.deck.draw())
            
        else:
            self.do_turn_shell()
        
        self.check_reverse()

        if self._battle:
            self._battle_count += 1
            print(f"BATTLE COUNT {self._battle_count}")
        else:
            self._battle_count = 0

        self.check_skip()

        print(self.pile.current_card.is_active)

        if not self.check_color_status() and self.pile.current_card.is_active and not self._battle:
            self._current_color = self._read_color()
            self.pile.current_card.deactivate()
            self._color_status = True
        # else:
        #     self._current_color = self.current_color
    
    def check_color_status(self) -> bool:
        if (self.pile.current_card.color is not None and self._current_color is not None):
            return True
        else:
            return False
    
    def check_winner(self) -> None:
        player, winner = self.rules.check_winner(self.players)
        if winner:
            self.ui.display_winner(winner_name=player.name)
            self.cycle.remove_player(player)
    
    def check_deck(self) -> None:
        if not len(self.deck):
            self.deck.reset(self.pile.back_to_deck())
    
    def check_valid_battle_card(self, player_card: Card, pile_card: Card) -> bool:
        return self.rules.check_battle(card1=player_card, card2=pile_card)
    
    def check_battle_card(self, card: Card) -> bool:
        return card.type is Type.BATTLE
    
    def check_first_card(self) -> None:
        if self.pile.current_card.action:
            self.start()

    def check_reverse(self) -> None:
        if self.pile.current_card.action == Actions.REVERSE:
            self.cycle.reverse_dir()
    
    def check_skip(self) -> None:
        if self.pile.current_card.action == Actions.SKIP:
            next(self.cycle)
    
    def check_battle(self) -> bool:
        if self.pile.current_card.type is Type.BATTLE:
            return True
        else:
            return False
    
    def check_wild(self, card: Card) -> bool:
        return card.action is Actions.WILD
    
    def check_draw4(self, card: Card) -> bool:
        return card.action is Actions.DRAW4
    
    def check_color_not_none(self) -> bool:
        if (self.pile.current_card.action is Actions.WILD and self.current_color is None):
            return True
            
        elif (self.pile.current_card.action is Actions.DRAW4 and self._battle is None and self.current_color is None):
            return True
        
        else:
            return False

    def hand_out_cards(self) -> None:
        for player in self.cycle.players:
            cards = self.deck.deal(self.n_cards)
            player.hand.set(cards=cards)
    
    def _read_color(self) -> Colors:
        color_name = self.ui.read_color().upper()
        return Colors[color_name]
    
    def _buy_x_cards(self, player_name: str, number: int, n_cards: int) -> str:
                """Generates a string describing the number of cards drawn"""
                return f"{player_name} has bought {number * n_cards} cards"
    