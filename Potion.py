"""@package docstring
Classes for all potions.

Potions are consumable items that either restore lost resources or cure persistent statuses.
All potions are "beltable", meaning they can be stored in the quick-slots granted by belts.
"""


import Item


class Potion (Item):
    pass


class HealingPotion (Potion):
    pass


class ManaPotion (Potion):
    pass


class RejuvPotion (Potion):
    pass


class StaminaPotion (Potion):
    pass


class AntidotePotion (Potion):
    pass


class ThawingPotion (Potion):
    pass
