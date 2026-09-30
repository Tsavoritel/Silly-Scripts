#mod01 excercise1, mod02 excercise2, and project 1-3
import random
from typing import Union
import time

usrname = input("Enter your name: ")
usrSelection = ""
items = []
dungeoned = False

# Age Check
try:
    age = int(input("...and your age? "))
except:
    print("Please input a whole number.")
if age < 13:
    print("You are a minor, and are not yet old enough to use this product")
    print("Shutting down...")
    exit

# Main Setup
# Entities
class SpecialTile():
    def __init__(self, display, isStaircase: bool, down: bool = False):
        self.display = display
        self.isStaircase = isStaircase
        self.down = down
class Player():
    def __init__(self, name, level, hp, spd, evasionchance):
        self.display = "☺︎"
        self.inventory = []
        self.name = name
        self.level = level
        self.hp = hp
        self.spd = spd
        self.evasionchance = evasionchance
class Enemy():
    def __init__(self, name, hp, atk, spd):
        self.display = "%"
        self.name = name
        self.hp = hp
        self.atk = atk
        self.spd = spd
class Item():
    def __init__(self, name, atk):
        self.display = "$"
        self.name = name
        self.atk = atk
class EmptyTile():
    def __init__(self):
        self.display = "-"

# Places
#class Tile():
#    def __init__(self, occupency: Union[Player, Enemy, SpecialTile, EmptyTile]):
#        self.occupency = occupency
class Hallway():
    def __init__(self):
        self.tiles: list = []
        self.maxEnemies: int
        self.tilesDisplay: list[str] = []
    def BuildHallway(self):
        self.maxEnemies = len(self.tiles) - 2
        self.tiles.append(SpecialTile(True, False))
        self.tilesDisplay.append("↑")
        self.tilesDisplay.append(specialTiles[0].display) # this wants to be an object, do you need a class?
        for i in range(random.randrange(2, 10)):
            if (random.randrange(1, 10) > 7): # Should u spawn an enemy
                enemyToSpawn: Enemy = enemies[random.randrange(0, len(enemies))] # Which one
                self.tiles.append(enemyToSpawn)
                self.tilesDisplay.append(enemyToSpawn.display)
            else:
                self.tiles.append(EmptyTile)
                self.tilesDisplay.append(specialTiles[2].display)
        self.tiles.append(SpecialTile(True, True))
        self.tilesDisplay.append(specialTiles[1].display)
        self.tilesDisplay.append("↓")
class Dungeon():
    def __init__(self, name, maxFloors, damageMod):
        self.name = name
        self.maxFloors: int = maxFloors
        self.damageMod = damageMod
        self.floors: list[Hallway] = []
    def BuildDungeon(self):
        i = 0
        for hall in range(self.maxFloors):
            hall = Hallway()
            hall.BuildHallway()
            self.floors.append(hall)
            print(f"Bult hallway: {i}: {hall.tilesDisplay}")
            i += 1


def ItemAdder(item):
    items.append(item)
def CheckInventory():
    print(items)
def PlayerInfo():
    print(f"You are {usrname} and are {age} years old.")
def DisplayOptions():
    optionsList = []
    curDungeon: int
    curFloor: int = 0
    global dungeoned
    if (dungeoned == False):
        optionsList.append("e: enter dungeon")
    else:
        print()
        optionsList.append("<: walk left")
        optionsList.append(">: walk right")
    optionsList.append("i: inventory")
    optionsList.append("p: playerinfo")
    optionsList.append("x: exit game")
    print(f"options: {optionsList}")
    usrSelection = input("Input: ")
    match usrSelection:
        case "e":
            print("Which dungeon would you like to explore ?")
            print(f"Options: 1: {dungeons[0].name}, 2: {dungeons[1].name}, 3: {dungeons[2].name}")
            try:
                curDungeon = int(input("Input: "))
            except:
                print("Invalid option")
                DisplayOptions()
            if not(curDungeon in (1, 2, 3)):
                print("Invalid option")
                DisplayOptions()
            curDungeon -= 1
            print(f"Entering {dungeons[curDungeon].name} ....")
            dungeons[curDungeon].BuildDungeon()
            time.sleep(1)
            print(f"Currently in: {dungeons[curDungeon].name}.. On floor {curFloor}")
            print(dungeons[curDungeon].floors[curFloor].tilesDisplay)
            dungeoned = True
            DisplayOptions()
        case "i":
            CheckInventory()
        case "p":
            PlayerInfo()
        case "<":
            print("Walked one space left")
        case ">":
            print("Walked one space right")
        case "x":
            print("Exiting...")
        case _:
            print("Invalid option, please choose from the following list")
            DisplayOptions()

# objects
enemies = []
enemies.append(Enemy("slime", 1, 0, 1))
enemies.append(Enemy("skeleton", 1.5, 1, 1))
enemies.append(Enemy("ghost", 2, 2, 2))

dungeons: list[Dungeon] = []
dungeons.append(Dungeon("Moss Grotto", random.randrange(2, 3), 1))
dungeons.append(Dungeon("Withered Catacombs", random.randrange(3, 5), 1.5))
dungeons.append(Dungeon("Fiery Hollows", random.randrange(4, 6), 2))

specialTiles: list[SpecialTile] = []
specialTiles.append(SpecialTile("=", True, False))
specialTiles.append(SpecialTile("=", True, True))
specialTiles.append(SpecialTile("-", False))

# main program (Start Game !)

print(f"Hello {usrname}, age {age} !")
print("You find yourself in a mysterious world of Goo, surrounded by vast fields and forests, you wander around in awe")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you feel compelled to walk in")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("In this world, the choice is yours, what is it you'd like to do?")

DisplayOptions()