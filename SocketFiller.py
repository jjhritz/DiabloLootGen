"""@package docstring
Classes for items that can be put in sockets.

Some weapons and armor have "sockets", slots that can accept gems, jewels, and runes.  Such items put into sockets
add new properties to the socketed equipment.
"""


import Item


class SocketFiller (Item):
    pass


class Jewel (SocketFiller):
    pass


class Rune (SocketFiller):
    pass
