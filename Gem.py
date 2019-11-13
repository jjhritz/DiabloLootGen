"""@package docstring
Classes for gems, both quality and type.  Includes Skulls.

Gems have both a type that determines what magical effects it provides and a quality that determines the magnitude
of those effects.  The game files represent both of those components separately as distinct groups and thus they are
represented by distinct classes here.  However, this may prove irrelevant for the purposes of this program and could
therefore be simplified.
"""


from SocketFiller import SocketFiller


class Gem (SocketFiller):
    pass


class ChippedGem (Gem):
    pass


class FlawedGem (Gem):
    pass


class StandardGem (Gem):
    pass


class FlawlessGem (Gem):
    pass


class PerfectGem (Gem):
    pass


class Amethyst (Gem):
    pass


class Diamond (Gem):
    pass


class Emerald (Gem):
    pass


class Ruby (Gem):
    pass


class Sapphire (Gem):
    pass


class Topaz (Gem):
    pass


class Skill (Gem):
    pass
