# Diablo 2 Item Roller

A stupid little knick-knack to knock some of the rust off my Python, loosely inspired by [this UPenn homework assignment](https://www.cis.upenn.edu/~cis110/11fa/hw/hw06/index.html).  It takes the data from the Diablo 2 files and uses it to implement the (ridiculously over-complicated) item generation algorithm as documented [here](https://diablo2.diablowiki.net/Item_Generation_Tutorial).  The ultimate goal is to get as close as possible to simulating the loot drops from killing a particular monster, including the randomized stats of items while remaining "rules-legal". 

In future I may add in options to extract statistical information, just for my own edification, but in the meantime there are already tools for that.  If you just want to know the best monsters to farm for an item, use [Dropcalc](http://dropcalc.silospen.com/item.php).  You'll not find something more useful here.
## How it works
1) Read in the contents of `ItemTypes.txt`, `ItemRatio.txt`, `armor.txt`, `weapons.txt`, `misc.txt`, `Magicprefix.txt`, and `Magicsuffix.txt`.  These all define the various kinds of items in the game and their statistics, necessary for representing the items in the code.  Ideally, the program will extract these files from the game's MPQ archives, but for the time being these files will need to be included as loose files.  

2) Generate the TCs defined at runtime.  The TCs for non-magic armor and weapons aren't stored in the game files; the game creates them when it launches, breaking the armor and weapons into groups spanning 3 levels each (e.g. all weapons of level 1 to 3 go in one group, weapons of level 4 to 6 go in another, etc.).

3) Read in the contents of `TreasureClassEx.txt`.  This is where the game's loot pools ("Treasure Classes" or "TCs") are defined.  Each monster is assigned a TC, so the TCs need to be constructed before the monsters.  Some TCs are recursive.

4) Read in the contents of `monstats.txt`.  This is where the TCs of monsters are defined.

5) Initialize the user interface.  This will be a CLI for the immediate future, but a GUI is planned.

6) Prompt the user for a monster to kill.  

7) Get the monster's number of "picks" to determine how many times to roll for loot.

8) For each pick, iterate through each TC until a item is selected or the dice come up as `NoDrop`.

9) When an item is a selected, determine its quality (Superior, Magic, Rare, Set, Unique).  This is where the player's Magic Find stat is checked.

10) Determine the item's level (`ilvl`).  

11) If the quality check determined a Set or Unique item, the list of Set and Unique items is consulted to find a random item of the appropriate type and level.

    I) If there is not a unique of that type, a rare item with triple durability will generate. 
    
    II) If there is no set item of the selected type, a magical item with double durability will appear.

12) Generate item Affixes (if possible).

13) Apply item properties (if any).

14) Format the item's properties for display.

15) Prompt the user to kill another of the same monster, select a new monster to kill, or exit the program.