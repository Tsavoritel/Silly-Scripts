#mod01 excercise1, mod02 excercise2, and project 1-3
import random
from typing import Union
import time

usrname = input("Enter your name: ")
age: int = 0
usrSelection = ""
items = []
dungeoned = False

curDungeon: int = 0
curFloor: int = 0
curTile: int = 1

def AgeCheck():
    global age
    try:
        age = int(input("...and your age? "))
    except:
        print("Please input a whole number.")
    if age < 13:
        print("You are a minor, and are not yet old enough to use this product")
        print("Restarting...")
        AgeCheck()
AgeCheck()

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
        self.tilesDisplay.append("↑")
        self.tiles.append(specialTiles[0]) # staircase up
        self.tilesDisplay.append(specialTiles[0].display)
        self.tiles.append(specialTiles[2]) # always make an empty space for player to spawn on
        self.tilesDisplay.append(specialTiles[2].display)
        for i in range(random.randrange(2, 10)):
            if (random.randrange(1, 10) > 7): # Spawn an enemy ?
                enemyToSpawn: Enemy = enemies[random.randrange(0, len(enemies))] # Which one
                self.tiles.append(enemyToSpawn)
                self.tilesDisplay.append(enemyToSpawn.display)
            else:
                self.tiles.append(specialTiles[2])
                self.tilesDisplay.append(specialTiles[2].display)
        self.tiles.append(specialTiles[1])
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
            #print(f"Bult hallway: {i}: {hall.tilesDisplay}") # tis for debugging
            i += 1

def ItemAdder(item):
    items.append(item)
def CheckInventory():
    print(items)
    DisplayOptions()
def PlayerInfo():
    print(f"{player.name}'s stats:")
    print(f"Hp: {player.hp}, Lv: {player.level}, Sp: {player.spd}")
    DisplayOptions()
def DisplayOptions():
    optionsList = []
    global dungeoned
    global curDungeon
    global curFloor
    global curTile
    if (dungeoned == False):
        optionsList.append("e: enter dungeon")
    else:
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
        print(f"Currently in: {dungeons[curDungeon].name}, basement {curFloor+1}")
        print(*dungeons[curDungeon].floors[curFloor].tilesDisplay)
        optionsList.append("<: walk left")
        optionsList.append(">: walk right")
    optionsList.append("i: inventory")
    optionsList.append("p: playerinfo")
    optionsList.append("x: exit game")
    print(f"options: {optionsList}")
    usrSelection = input("Input: ")
    match usrSelection:
        case "e":
            if (dungeoned): DisplayOptions()
            print("Which dungeon would you like to explore ?")
            print(f"Options: 1: {dungeons[0].name}, 2: {dungeons[1].name}, 3: {dungeons[2].name}")
            try:
                curDungeon = int(input("Input: "))
            except ValueError:
                print("Invalid option")
                DisplayOptions()
            if not(curDungeon in (1, 2, 3)):
                print("Invalid option")
                DisplayOptions()
            curDungeon -= 1
            print(f"Entering {dungeons[curDungeon].name} ....")
            dungeons[curDungeon].BuildDungeon()
            time.sleep(1)
            dungeoned = True
            DisplayOptions()
        case "i":
            CheckInventory()
        case "p":
            PlayerInfo()
        case "<":
            if dungeons[curDungeon].floors[curFloor].tiles[curTile - 1] == specialTiles[2]:
                print("Walked one space left")
                curTile += 1
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile - 1] = player.display
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
                curTile -= 2
                print(f"Current Tile: {curTile}")
            else: #has to be staircase up
                if (curFloor - 1 >= 0):
                    curFloor -= 1
                    curTile -= 1
                    print("Returning to last floor...")
                    curTile = len(dungeons[curDungeon].floors[curFloor].tiles) - 1
                else:
                    print("you exited the dungeon") # maybe generate the amount based on how many tiles you passed
                    dungeoned = False
            DisplayOptions()
        case ">":
            if type(dungeons[curDungeon].floors[curFloor].tiles[curTile+1]) == Enemy:
                #would like to enable the option to check enemy stats
                enemy = dungeons[curDungeon].floors[curFloor].tiles[curTile+1].name
                print(f"Attacked an {enemy} !!")
            elif dungeons[curDungeon].floors[curFloor].tiles[curTile+1] == specialTiles[2]:
                print("Walked one space right")
                curTile += 1
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
                print(f"Current Tile: {curTile}")
            else: #has to be staircase down
                print("Entering next floor...")
                try:
                    dungeons[curDungeon].floors[curFloor + 1]
                except:
                    print("you get the rock food !!") # maybe generate the amount based on how many tiles you passed
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile + 1] = specialTiles[2].display
                curFloor += 1
                curTile = 1
            DisplayOptions()

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

player = Player(usrname, 0, 5, 1, 0)

# main program, Start Game !

print(f"Hello {usrname}, age {age} !")
print("You find yourself in a mysterious world of Goo")
print("Surrounded by vast fields and forests, remembering you were entrusted to save the village")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you are compelled inward")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("In this world, the choice is yours, what is it you'd like to do?")

DisplayOptions()

# pieces of lore handed to you throughout the game
#print("Awhile ago, the village faced tragidy with a flood that completely destroyed all sources of food and farm land")