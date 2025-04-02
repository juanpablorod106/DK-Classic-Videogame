# game.py
from player import Player
from flame import Flame
from ladder import Ladder
from hammer import Hammer
from bridge import Bridge
from barrel import Barrel

def setup_game():
    player = Player()
    hammer = Hammer()
    barrel = Barrel()
    bridge = Bridge()
    ladder = Ladder()
    flame = Flame()

    return player, hammer, barrel, bridge, ladder, flame