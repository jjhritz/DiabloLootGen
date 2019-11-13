"""@package docstring
Classes for Amulets and rings.

Amulets are rings have their own equip slots and, unlike armor and weapons, are always of at least Magic quality.
"""

from Item import Equipment
from Misc import Misc


class Amulet(Equipment, Misc):
    pass


class Ring(Equipment, Misc):
    pass
