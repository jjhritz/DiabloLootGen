"""@package docstring
All melee weapons that deal blunt damage, including wands and staves.

Blunt weapons are distinct from other weapons in that they deal +50% damage to undead, even without enchantments.
A distinct superclass allows this property to be passed on by inheritance.
"""


from MeleeWeap import MeleeWeap


class BluntWeap (MeleeWeap):
    pass


class RodWeap (BluntWeap):
    pass


class Scepter (RodWeap):
    pass


class Wand (RodWeap):
    pass


class Staff (RodWeap):
    pass


class Club (BluntWeap):
    pass


class Hammer (BluntWeap):
    pass


class Mace (BluntWeap):
    pass
