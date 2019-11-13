"""@package docstring
Superclasses for all loot in the game.

Items are the overall classification for all the stuff you pick up in the game.  Weapons, keys, potions, everything.
Items all have a set of common attributes that need to be inherited.
"""


class Item:
    pass


class Equipment (Item):
    pass


class Quest (Item):
    pass
