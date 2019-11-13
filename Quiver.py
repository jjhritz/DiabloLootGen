"""@package docstring
Classes for missile weapon ammunition.

Quivers of arrows feed bows and quivers of bolts feed crossbows (xbows).
"""


from Item import Equipment


class Quiver (Equipment):
    pass


class BowQuiver (Quiver):
    pass


class XbowQuiver (Quiver):
    pass
