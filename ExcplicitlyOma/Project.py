#mod01 excercise1, mod02 excercise2, and project 1-3
import random
from typing import Union

usrname = input("Enter your name: ")
usrSelection = ""
items = []
dungeoned = False
fighting = False

#age check

try:
    age = int(input("...and your age? "))
except:
    print("Please input a whole number.")
if age < 13:
    print("You are a minor, and are not yet old enough to use this product")
    print("Shutting down...")
    exit

# Main Setup
# Places
class Dungeon():
    def __init__(self, name, floors, damageMod):
        self.name = name
        self.floors = floors
        self.damageMod = damageMod
class Hallway():
    def __init__(self, tiles, maxEnemies):
        self.tiles = tiles
        self.maxEnemies = maxEnemies
    def BuildHallway(self):
        self.tiles = []
        self.maxEnemies = self.tiles - 2
        self.tiles.append(Tile(Staircase(EmptyTile)))
        for i in random.randrange(2, 10):
            i += 1
            if (random.randrange(1, 10) > 7): # Should u spawn an enemy
                enemyToSpawn: Enemy = enemies[random.randrange(1, enemies.count + 1)] # Which one
                self.tiles.append(Tile(enemyToSpawn))
            else:
                self.tiles.append(Tile(EmptyTile))
        self.tiles.append(Tile(Staircase(True)))
class Tile():
    def __init__(self, occupency: Union[Player, Enemy, Staircase, EmptyTile]):
        self.occupency = occupency

# Entities
class Staircase():
    def __init__(self, down: bool):
        self.display = "="
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

def ItemAdder(item):
    items.append(item)
def CheckInventory():
    print(items)
def PlayerInfo():
    print(f"You are {usrname} and are {age} years old.")
def DisplayOptions():
    optionsList = []
    if (dungeoned == False):
        optionsList.append("e: enter dungeon")
    else:
        optionsList.append("<: walk left")
        optionsList.append(">: walk right")
    if (fighting == True):
        optionsList.append("a: attack enemy")
    optionsList.append("i: inventory")
    optionsList.append("p: playerinfo")
    optionsList.append("x: exit game")
    print(f"options: {optionsList}")
    usrSelection = input("Input: ")
    match usrSelection:
        case "e":
            print("Which dungeon would you like to explore ?")
            print(f"Options: 1: {dungeons[0].name}, 2: {dungeons[1].name}, 3: {dungeons[2].name}")
            i = input("Input: ")
            if not(i in ("1", "2", "3")):
                print("Invalid option")
                DisplayOptions()
            print(f"Entering {dungeons[int(i)-1].name} ....")
            dungeoned == True
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

# main program (Start Game !)

print(f"Hello {usrname}, age {age} !")
print("You find yourself in a mysterious world of Goo, surrounded by vast fields and forests, you wander around in awe")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you feel compelled to walk in")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("In this world, the choice is yours, what is it you'd like to do?")

DisplayOptions()