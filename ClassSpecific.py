"""@package docstring
Classes for all character class-specific items.

Each character class has certain items no other class can use, such as the Paladin's auric shields.
This allows the item to be given magical properties useful only to that particular class.
"""


from Item import Item
from MeleeWeap import MeleeWeap, Spear
from MissileWeap import Bow
from ThrownWeap import Javelin
from Armor import Helm, BodyArmor, Shield


class ClassSpecific (Item):
    pass


class AmazonItem (ClassSpecific):
    pass


class BarbarianItem (ClassSpecific):
    pass


class NecromancerItem (ClassSpecific):
    pass


class PaladinItem (ClassSpecific):
    pass


class SorceressItem (ClassSpecific):
    pass


class AssassinItem (ClassSpecific):
    pass


class DruidItem (ClassSpecific):
    pass


class HandToHand (AssassinItem, MeleeWeap):
    pass


class SorcOrb (SorceressItem, MeleeWeap):
    pass


class VoodooHead (NecromancerItem, Shield):
    pass


class AuricShield (PaladinItem, Shield):
    pass


class PrimalHelm (BarbarianItem, Helm):
    pass


class DruidPelt (DruidItem, Helm):
    pass


class AssassinCloak (AssassinItem, BodyArmor):
    pass


class AmazonBow (AmazonItem, Bow):
    pass


class AmazonSpear (AmazonItem, Spear):
    pass


class AmazonJavelin (AmazonItem, Javelin):
    pass
