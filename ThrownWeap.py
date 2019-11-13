"""@package docstring
Classes for weapons that can be thrown, including those that can also be used for melee attacks.
"""


import Weap
from MeleeWeap import MeleeWeap, Knife, Axe, Spear


class ThrownWeap (Weap):
    pass


class ComboWeap (ThrownWeap, MeleeWeap):
    pass


class ThrownPot (ThrownWeap):
    pass


class ThrownKnife (ComboWeap, Knife):
    pass


class ThrownAxe (ComboWeap, Axe):
    pass


class Javelin (ComboWeap, Spear):
    pass
