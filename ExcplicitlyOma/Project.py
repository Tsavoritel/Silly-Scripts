#mod01 excercise1, mod02 excercise2, and project 1-3
import random
from typing import Union
import time

usrname = input("Enter your name: ")
age: int = 0
usrSelection = ""
items = []

inDungeon = False
fighting = False


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
    def __init__(self, name, level, xp, hp, maxHp, spd, atk, evasionchance, heldRockmeal = 0):
        self.display = "☺︎"
        self.inventory = []
        self.name = name
        self.level = level
        self.xp = xp
        self.hp = hp
        self.maxHp = maxHp
        self.spd = spd
        self.atk = atk
        self.evasionchance = evasionchance
        self.heldRockmeal = heldRockmeal
    def PlayerInfo(self):
        print(f"{self.name}'s stats:")
        print(f"Hp: {self.hp}, Lv: {self.level} (xp:{self.xp}/20), At: {self.atk}, Sp: {self.spd}, Hr: {self.heldRockmeal}")
    def LevelUp(self):
        print("You leveled up !!")
        self.atk += 0.5
        self.spd += 0.5
        self.evasionchance += 2
        self.maxHp += 2
        self.level += 1
        self.xp = 0
class Enemy():
    def __init__(self, name, hp, atk, spd, xp):
        self.display = "%"
        self.name = name
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.xp = xp
    def EnemyInfo(self):
        print(f"{self.name}'s stats:")
        print(f"Hp: {self.hp}")
class Item():
    def __init__(self, name, atk):
        self.display = "$"
        self.name = name
        self.atk = atk
class Village():
    def __init__(self, fednessLvl):
        self.fednessLvl = fednessLvl
        self.nextMileStone = 119
    def CheckDialogue(self):
        global curDungeon
        global inDungeon
        self.fednessLvl += player.heldRockmeal
        if self.fednessLvl > self.nextMileStone:
            self.fednessLvl = self.nextMileStone
        player.heldRockmeal = 0
        if self.fednessLvl <= 100:
            print('"Awhile ago, the village was faced with tragidy..\n' \
            'There was a flood that destroyed all of our sources of food and farm land"')
            self.nextMileStone = 120
        elif self.fednessLvl <= 120:
            print('"Oh my, is that food?? Bless you, you might have staved over our hunger for now.."')
            self.nextMileStone = 150
        elif self.fednessLvl <= 150:
            print('"I know it might feel wrong taking this food, but it is for the best."')
            self.nextMileStone = 200
        elif self.fednessLvl <= 200:
            print('"I have heard other townspeople complain about the dungeon raids as well...\n' \
            'The truth is, rockmeal is a neverending resource, but they choose to keep it all for themselves."')
            self.nextMileStone = 300
        elif self.fednessLvl <= 300:
            pass
            self.nextMileStone = 455
        elif self.fednessLvl <= 455:
            print('"Hahahaha !! We have too much food !! I believe our village is saved !!\n' \
            '..you... must have killed so many..."')
            self.nextMileStone = 600
        elif self.fednessLvl <= 600:
            print('"Ha..hah.. thats even more ! What could we.. possibly.. do with all of this food..?"')
            self.nextMileStone = 1000
        elif self.fednessLvl < 1000:
            print('"Why do you keep pillaging... we have enough, theres no need for any more..."')
            self.nextMileStone = 1500
        elif self.fednessLvl == 1500:
            curDungeon = 3
            print(f"Entering {dungeons[curDungeon].name} ....")
            dungeons[curDungeon].BuildDungeon()
            time.sleep(1)
            inDungeon = True
            DisplayOptions()
        if self.fednessLvl < 300:
            print('"We have nothing else for you now, besides healing, please do your best"')
        elif self.fednessLvl < 1500:
            print('"Take all the food you need, we have plenty now"')
        player.hp = player.maxHp
        print("You feel rested..")
        print(f"Next milestone: {self.nextMileStone}, current village fedness points: {self.fednessLvl}")
# Places
#class Tile():
#    def __init__(self, occupency: Union[Player, Enemy, SpecialTile, EmptyTile]):
#        self.occupency = occupency
class Hallway():
    def __init__(self):
        self.tiles: list = []
        self.maxEnemies: int
        self.maxTiles: int
        self.dmgMod: float = 1
        self.tilesDisplay: list[str] = []
    def BuildHallway(self, maxTiles, dmgMod):
        self.maxTiles = maxTiles
        self.dmgMod = dmgMod
        self.maxEnemies = len(self.tiles) - 2
        self.tilesDisplay.append("↑")
        self.tiles.append(specialTiles[0]) # staircase up
        self.tilesDisplay.append(specialTiles[0].display)
        self.tiles.append(specialTiles[2]) # always make an empty space for player to spawn on
        self.tilesDisplay.append(specialTiles[2].display)
        for i in range(random.randrange(2, self.maxTiles)):
            if (random.randrange(1, 10) > 7): # Spawn an enemy ?
                enemyToSpawn: Enemy = enemies[random.randrange(0, len(enemies))] # Which one
                enemyToSpawn.hp *= dmgMod
                self.tiles.append(enemyToSpawn)
                self.tilesDisplay.append(enemyToSpawn.display)
            else:
                self.tiles.append(specialTiles[2])
                self.tilesDisplay.append(specialTiles[2].display)
        self.tiles.append(specialTiles[1])
        self.tilesDisplay.append(specialTiles[1].display)
        self.tilesDisplay.append("↓")
class Dungeon():
    def __init__(self, name, maxFloors, damageMod, maxTilesPerFloor = 10):
        self.name = name
        self.maxFloors: int = maxFloors
        self.damageMod = damageMod
        self.floors: list[Hallway] = []
        self.maxTilesPerFloor = maxTilesPerFloor
    def BuildDungeon(self):
        self.floors.clear()
        i = 0
        for hall in range(self.maxFloors):
            hall = Hallway()
            hall.BuildHallway(self.maxTilesPerFloor, self.damageMod)
            self.floors.append(hall)
            #print(f"Bult hallway: {i}: {hall.tilesDisplay}") # tis for debugging
            i += 1

def ItemAdder(item):
    items.append(item)
def CheckInventory():
    print(items)
    DisplayOptions()
def DisplayOptions():
    optionsList = []
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    global curEnemy
    if (inDungeon == False):
        optionsList.append("e: enter dungeon")
        optionsList.append("v: visit village")
    else:
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
        print(f"Currently in: {dungeons[curDungeon].name}, basement {curFloor+1}")
        print(*dungeons[curDungeon].floors[curFloor].tilesDisplay)
        optionsList.append("<: walk left")
        optionsList.append(">: walk right")
    #optionsList.append("i: inventory")
    optionsList.append("p: player info")
    if (curEnemy != None):
        optionsList.append("e: enemy info")
    optionsList.append("x: exit game")
    print(f"options: {optionsList}")
    usrSelection = input("Input: ")
    print("+-----------------------------------------+")
    match usrSelection:
        case "e":
            if inDungeon == False:
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
                inDungeon = True
                DisplayOptions()
            elif curEnemy != None:
                curEnemy.EnemyInfo()
                DisplayOptions()
        case "v":
            if inDungeon == False:
                village.CheckDialogue()
                DisplayOptions()
        #case "i":
        #    CheckInventory()
        case "p":
            player.PlayerInfo()
            DisplayOptions()
        case "<":
            if inDungeon:
                MoveLeft()
        case ">":
            if inDungeon:
                MoveRight()
        case "x":
            print("Exiting...")
            quit()
        case _:
            pass
    print("Invalid option, please choose from the following list")
    DisplayOptions()

def MoveRight():
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    global curEnemy

    # Fight enemy if its in front of you
    if type(dungeons[curDungeon].floors[curFloor].tiles[curTile+1]) == Enemy:
        curEnemy = dungeons[curDungeon].floors[curFloor].tiles[curTile+1]
        FightEnemy()

    # Move forward if nothing is in front of you
    elif dungeons[curDungeon].floors[curFloor].tiles[curTile+1] == specialTiles[2]:
        print("Walked one space right")
        curTile += 1
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
        #print(f"Current Tile: {curTile}")

    # Has to be staircase down, so take it
    else:
        try:
            dungeons[curDungeon].floors[curFloor + 1]
        except:
            print("You reached the bottom and find rockmeal !")
            foundRockmeal = 0
            for i in range(len(dungeons[curDungeon].floors)):
                foundRockmeal += len(dungeons[curDungeon].floors[i].tiles)
            if curDungeon == 0:
                foundRockmeal //= 2
            elif curDungeon == 2:
                foundRockmeal *= 2
            print(f"You pickup {foundRockmeal} pieces !!")
            if player.heldRockmeal > 0:
                player.heldRockmeal = round(player.heldRockmeal * 1.1, None)
                print("Something lucky happened because you were risky !!")
            player.heldRockmeal += foundRockmeal
            curTile = 1
            curFloor = 0
            inDungeon = False
            DisplayOptions()
        print("Entering next floor...")
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile + 1] = specialTiles[2].display
        curFloor += 1
        curTile = 1
    DisplayOptions()

def MoveLeft():
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    if dungeons[curDungeon].floors[curFloor].tiles[curTile - 1] == specialTiles[2]:
        print("Walked one space left")
        curTile += 1
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile - 1] = player.display
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
        curTile -= 2
        #print(f"Current Tile: {curTile}")
    else: #has to be staircase up
        if (curFloor - 1 >= 0):
            curFloor -= 1
            curTile -= 1
            print("Returning to last floor...")
            curTile = len(dungeons[curDungeon].floors[curFloor].tiles) - 1
        else:
            print("You exited the dungeon") # maybe generate the amount based on how many tiles you passed
            inDungeon = False
    DisplayOptions()

def FightEnemy():
    global curEnemy
    global curTile
    global inDungeon
    if curEnemy.spd > player.spd and curEnemy.hp > 0 and player.hp > 0:
        if(random.randrange(1, 100) > player.evasionchance):
            player.hp -= curEnemy.atk
            print(f"Attacked by a {curEnemy.name} !!")
        else: print(f"You dodged {curEnemy.name}'s attack !!")
        curEnemy.hp -= player.atk
        print(f"Attacked a {curEnemy.name} !!")
    elif curEnemy.hp > 0 and player.hp > 0:
        curEnemy.hp -= player.atk
        print(f"Attacked a {curEnemy.name} !!")
        if curEnemy.hp > 0:
            player.hp -= curEnemy.atk
            print(f"Attacked by a {curEnemy.name} !!")
        else:
            EnemyDied()
    elif player.hp > 0:
        EnemyDied()
    if player.hp <= 0: 
        print("Ran out of energy and fainted...")
        print(f"Got carried away and lost {player.heldRockmeal} rockmeal...")
        player.heldRockmeal = 0
        curTile = 1
        inDungeon = False
        DisplayOptions()

def EnemyDied():
    global curDungeon
    global curFloor
    global curTile
    global curEnemy
    player.xp += curEnemy.xp
    if player.xp >= 20:
        player.LevelUp()
    print(f"You beat the {curEnemy.name} and gained {curEnemy.xp}xp !!")
    curEnemy = None
    dungeons[curDungeon].floors[curFloor].tiles[curTile+1] = specialTiles[2]
    dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+2] = specialTiles[2].display
    DisplayOptions()

# objects
enemies = []
enemies.append(Enemy("slime", 1, 0, 1, 1))
enemies.append(Enemy("skeleton", 1.5, 1, 1, 2))
enemies.append(Enemy("ghost", 2, 2, 2, 5))

dungeons: list[Dungeon] = []
dungeons.append(Dungeon("Moss Grotto", random.randrange(2, 3), 1, 8))
dungeons.append(Dungeon("Withered Catacombs", random.randrange(3, 5), 3,  12))
dungeons.append(Dungeon("Fiery Hollows", random.randrange(4, 6), 8, 16))
dungeons.append(Dungeon("...Village.. what are you doing??", 10, 20, 32))

specialTiles: list[SpecialTile] = []
specialTiles.append(SpecialTile("=", True, False))
specialTiles.append(SpecialTile("=", True, True))
specialTiles.append(SpecialTile("-", False))

player = Player(usrname, 1, 0, 5, 5, 1, 1, 1)
curEnemy: Enemy = None
village = Village(100)

# main program, Start Game !rest

print(f"Hello {usrname}, age {age} !")
if age > 120: 
    time.sleep(1)
    print("Wow.. you're *really* old !")
    time.sleep(1)
print("You find yourself in a mysterious world of Goo")
print("Surrounded by vast fields and forests, remembering you were entrusted to save the village")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you are compelled inward")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("In this world, the choice is yours, what is it you'd like to do?")

DisplayOptions()