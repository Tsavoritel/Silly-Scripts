#mod01 excercise1, mod02 excercise2, and project 1-3
import random
from typing import Union

usrname = input("Enter your name: ")
usrSelection = ""
items = []

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

# objects
enemies = []
enemies.append(Slime = Enemy("slime", 1, 0, 1))
enemies.append(Skeleton = Enemy("skeleton", 1.5, 1, 1))
enemies.append(Ghost = Enemy("ghost", 2, 2, 2))

# main program (Start Game !)

print(f"Hello {usrname}, age {age} !")
print("You find yourself in a mysterious world of Goo, surrounded by vast fields and forests, you wander around in awe")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you feel compelled to walk in")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("Which dungeon shall you delve ..?")

dungeoned == False
fighting == False
optionsList = []

while usrSelection != "exit":
    print("Options: gotitem, inventory, whoami, exit")
    usrSelection = input("Input: ")
    match usrSelection:
        case "gotitem":
            ItemAdder(input("What item did you pickup? "))
        case "inventory":
            CheckInventory()
        case "whoami":
            PlayerInfo()
        case "exit":
            print("Exiting...")
        case _:
            print("Invalid option, please choose from the following list")
