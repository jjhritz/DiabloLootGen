"""@package docstring
Classes for all non-class-specific armor types, including shields.

This covers torso armor, helms, boots, gloves, shields, belts, and circlets, but does not include class-specific armor.
Paladin shields, Barbarian helmets, and the like are defined in ClassSpecific.py.
"""

from Item import Equipment


class Armor (Equipment):
    pass


class BodyArmor (Armor):
    pass


class Boots (Armor):
    pass


class Gloves (Armor):
    pass


class Shield (Armor):
    pass


class Belt (Armor):
    pass


class Helm (Armor):
    pass


class Circlet (Helm):
    pass
