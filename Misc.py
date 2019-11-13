"""@package docstring
Classes for items that fit no other classification.

Miscellaneous items are neither armor nor weapons, and thus don't have properties like damage or durability.
"""


import Item


class Misc (Item):
    pass


class Gold (Misc):
    pass


class Herb (Misc):
    pass


class Elixir (Misc):
    pass


class Book (Misc):
    pass


class Torch (Misc):
    pass


class Scroll (Misc):
    pass


class Key (Misc):
    pass
