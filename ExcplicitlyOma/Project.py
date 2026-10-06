#mod01 excercise1, mod02 excercise2, project 1-4, and final project
import random
import copy
import time

usrSelection = ""
items = []

inDungeon = False
fighting = False
showMoreOptions = False
autoWalk = False

curDungeon: int = 0
curFloor: int = 0
curTile: int = 1

usrname = ""
age: int = 0

def CheckUsrName():
    global usrname
    usrname = input("Enter your name: ")
    if usrname == "":
        print("Come on, give a real name")
        CheckUsrName()

def AgeCheck():
    global age
    try:
        age = int(input("...and your age? "))
    except:
        print("Please input a whole number.")
    if age < 13:
        print("You are a minor, and are not yet old enough to use this product")
        print("Exiting...")
        quit()

CheckUsrName()
AgeCheck()

# Main Setup
# Entities
class SpecialTile(): #Tile is a piece of a hallway
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
        print(f"Hp: {self.hp}, Lv: {self.level} (xp:{self.xp}/20), At: {self.atk}, Sp: {self.spd}, Rm: {self.heldRockmeal}")
    def LevelUp(self):
        print("| +------------- You leveled up !! -------------+ |")
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
        print(f"Hp: {self.hp}, At: {self.atk}")

class Village(): # Village dialogue and stats
    def __init__(self, fednessLvl):
        self.fednessLvl = fednessLvl
        self.nextMileStone = 100
    def CheckDialogue(self):
        global curDungeon
        global inDungeon
        self.fednessLvl += player.heldRockmeal
        if self.fednessLvl > self.nextMileStone:
            self.fednessLvl = self.nextMileStone
        player.heldRockmeal = 0
        if self.fednessLvl >= 50 and self.fednessLvl < 100:
            print('"Awhile ago, the village was faced with tragidy..\n' \
            'There was a flood that destroyed all of our sources of food and farm land"')
            self.nextMileStone = 100
        elif self.fednessLvl >= 100 and self.fednessLvl < 120:
            print('"Oh my, is that food?? Bless you, you might have staved over our hunger for now.."')
            self.nextMileStone = 120
        elif self.fednessLvl >= 120 and self.fednessLvl < 150:
            print('"I know it might feel wrong taking this food, but it is for the best."')
            self.nextMileStone = 150
        elif self.fednessLvl >= 150 and self.fednessLvl < 200:
            print('"I have heard other townspeople complain about the dungeon raids as well...\n' \
            'The truth is, rockmeal is a neverending resource, but they choose to keep it all for themselves."')
            self.nextMileStone = 200
        elif self.fednessLvl >= 200 and self.fednessLvl < 300:
            pass
            self.nextMileStone = 300
        elif self.fednessLvl >= 300 and self.fednessLvl < 455:
            print('"Hahahaha !! We have too much food !! I believe our village is saved !!\n' \
            '..you... must have killed so many..."')
            self.nextMileStone = 455
        elif self.fednessLvl >= 455 and self.fednessLvl < 600:
            print('"Ha..hah.. thats even more ! What could we.. possibly.. do with all of this food..?"')
            self.nextMileStone = 600
        elif self.fednessLvl >= 600 and self.fednessLvl < 1000:
            print('"Why do you keep pillaging... we have enough, theres no need for any more..."')
            self.nextMileStone = 1000
        elif self.fednessLvl >= 1000 and self.fednessLvl < 1500:
            curDungeon = 3
            print(f"Entering {dungeons[curDungeon].name} ....")
            dungeons[curDungeon].BuildDungeon()
            time.sleep(1)
            inDungeon = True
            self.nextMileStone = 1500
            return
        else:
            print("Theres nothing here.")
            return
        if self.fednessLvl < 200:
            print('"We have nothing else for you now, besides healing, please do your best"')
        elif self.fednessLvl < 600:
            print('"Take all the food you need, we have plenty now"')
        else:
            print("...")
        player.hp = player.maxHp
        print("You feel rested..")
        print(f"Next milestone: {self.nextMileStone}, current village fedness points: {self.fednessLvl}")
# Places
class Hallway():
    def __init__(self):
        self.tiles: list = []
        self.maxEnemies: int
        self.maxTiles: int
        self.tilesDisplay: list[str] = []
    def BuildHallway(self, maxTiles):
        # within each hallway there are some static tiles, and random between enemies and empty tiles
        self.maxTiles = maxTiles
        self.maxEnemies = len(self.tiles) - 2
        self.tilesDisplay.append("↑")
        self.tiles.append(specialTiles[0]) # staircase up
        self.tilesDisplay.append(specialTiles[0].display)
        self.tiles.append(specialTiles[2]) # always make an empty space for player to spawn on
        self.tilesDisplay.append(specialTiles[2].display)

        for i in range(random.randrange(2, self.maxTiles)):
            if (random.randrange(1, 10) > 6): # Spawn an enemy ?
                if curDungeon != 3:
                    enemyToSpawn = copy.copy(enemies[random.randrange(0, len(enemies))]) # Which one
                else:
                    enemyToSpawn = copy.copy(villager)
                    print("what have you done...")
                enemyToSpawn.hp *= dungeons[curDungeon].damageMod
                self.tiles.append(enemyToSpawn)
                self.tilesDisplay.append(enemyToSpawn.display)
            else: # place an empty tile
                self.tiles.append(specialTiles[2])
                self.tilesDisplay.append(specialTiles[2].display)
        self.tiles.append(specialTiles[1]) # staircase down
        self.tilesDisplay.append(specialTiles[1].display)
        self.tilesDisplay.append("↓")

class Dungeon():
    def __init__(self, name, maxFloors, damageMod, maxTilesPerFloor = 10):
        self.name = name
        self.maxFloors: int = maxFloors
        self.damageMod = damageMod
        self.floors: list[Hallway] = []
        self.maxTilesPerFloor = maxTilesPerFloor
    def BuildDungeon(self): # for each floor a dungeon should have, generate a hallway
        self.floors.clear()
        i = 0
        for hall in range(self.maxFloors):
            hall = Hallway()
            hall.BuildHallway(self.maxTilesPerFloor)
            self.floors.append(hall)
            i += 1
def DisplayOptions():
    optionsList = []
    global showMoreOptions
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    global curEnemy

    # Build options list based on players situation
    print("")
    if (inDungeon == False):
        optionsList.append("e: enter dungeon")
        optionsList.append("v: visit village")
    else:
        dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
        print(f"Currently in: {dungeons[curDungeon].name}, basement {curFloor+1}")
        print(*dungeons[curDungeon].floors[curFloor].tilesDisplay)
        optionsList.append("<: walk left")
        optionsList.append(">: walk right")
    optionsList.append("p: player info")
    if (curEnemy != None):
        optionsList.append("e: enemy info")
    if (showMoreOptions == True):
        if village.fednessLvl >= 200 and village.fednessLvl < 455:
            optionsList.append("x: complete objective")
        else:
            optionsList.append("x: exit game")
        optionsList.append("i: info")
        optionsList.append("s: settings")
    else: optionsList.append("m: more options")

    # Give options and handle input
    print(f"options: {optionsList}")
    usrSelection = input("Input: ")
    showMoreOptions = False
    print("")
    print("+-------------------------------------------------+")
    match usrSelection:
        case "e":
            if inDungeon == False:
                # this means a user is not in a dungeon, and would like to be in one
                # so lets go ahead and ask for which one and generate it
                print("Which dungeon would you like to explore ?")
                print(f"Options: 1: {dungeons[0].name}, 2: {dungeons[1].name}, 3: {dungeons[2].name}")
                try:
                    curDungeon = int(input("Input: "))
                except ValueError:
                    print("Invalid option")
                    return
                if not(curDungeon in (1, 2, 3)):
                    print("Invalid option")
                    return
                curDungeon -= 1
                curTile = 1
                curFloor = 0
                print(f"Entering {dungeons[curDungeon].name} ....")
                dungeons[curDungeon].BuildDungeon()
                time.sleep(1)
                inDungeon = True
            elif curEnemy != None:
                curEnemy.EnemyInfo()
        case "v":
            if inDungeon == False:
                village.CheckDialogue()
            else: print("Invalid option, please choose from the following list")
        case "p":
            player.PlayerInfo()
        case "m":
            showMoreOptions = True
        case "i":
            print("Controls:")
            print("move leftward: < , a")
            print("move rightward: > . d")
            print("Tips:")
            print("To attack an enemy, walk into it")
            print("You can leave a dungeon by walking out of it")
            print("Options are always available on context")
        case "s":
            Settings()
        case "<" | "," | "a":
            if inDungeon:
                MoveLeft()
            else: print("Invalid option, please choose from the following list")
        case ">" | "." | "d":
            if inDungeon:
                MoveRight()
            else: print("Invalid option, please choose from the following list")
        case "x":
            if village.fednessLvl > 200 and village.fednessLvl < 455:
                print("You go back home to rest, with the rockmeal evergrowing, food will never be a concern for anyone agian.")
            print("Exiting...")
            quit()
        case "=":
            village.fednessLvl += 50
        case "+":
            player.LevelUp()
        case _:
            print("Invalid option, please choose from the following list")

def MoveRight():
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    global curEnemy
    dcf = dungeons[curDungeon].floors[curFloor].tiles

    # Move forward if nothing is in front of you
    if type(dcf[curTile+1]) == SpecialTile:
        if dcf[curTile+1].isStaircase == False:
            i = 0
            while dcf[curTile+1].isStaircase == False:
                i += 1
                curTile += 1
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
                dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile+1] = player.display
                if autoWalk == False or type(dcf[curTile+1]) != SpecialTile or dcf[curTile+1].isStaircase == True:
                    break
            print(f"Walked {i} space(s) right")
        # Take staircase down if a staircase is in front of you
        elif dcf[curTile+1].isStaircase == True:
            try:
                dungeons[curDungeon].floors[curFloor + 1]
            except: # if this is the bottom floor, then teleport back to the top and award rockmeal
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
                inDungeon = False
                return
            print("Entering next floor...")
            dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile + 1] = specialTiles[2].display
            curFloor += 1
            curTile = 1
    # Fight enemy if its in front of you
    elif type(dcf[curTile+1]) == Enemy:
        curEnemy = dcf[curTile+1]
        FightEnemy()

def MoveLeft(): # follows the same logic as moving right, just with going back and up as needed
    global inDungeon
    global curDungeon
    global curFloor
    global curTile
    global curEnemy
    dcf = dungeons[curDungeon].floors[curFloor].tiles

    if type(dcf[curTile - 1]) != SpecialTile: return
    if dcf[curTile - 1].isStaircase == False:
        i = 1
        while dcf[curTile - 1] == specialTiles[2]:
            i += 1
            curTile += 1
            dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile - 1] = player.display
            dungeons[curDungeon].floors[curFloor].tilesDisplay[curTile] = specialTiles[2].display
            curTile -= 2
            if autoWalk == False:
                break
        print(f"Walked {i} space(s) left")
    elif dcf[curTile-1].isStaircase == True:
        if (curFloor - 1 >= 0):
            curFloor -= 1
            curTile -= 1
            print("Returning to last floor...")
            curTile = len(dungeons[curDungeon].floors[curFloor].tiles) - 2
        else:
            print("You exited the dungeon") # maybe generate the amount based on how many tiles you passed
            curEnemy = None
            inDungeon = False

def FightEnemy():
    global curEnemy
    global curTile
    global curFloor
    global inDungeon

    # checks player stats against theirs and follows with damage on both sides
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
        curFloor = 0
        inDungeon = False

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

def Settings():
    global autoWalk
    print(f"a: Toggle autowalk - {autoWalk}")
    print(f"press anything else to exit")
    si = input("Toggle setting: ")
    match si:
        case "a":
            autoWalk = not autoWalk
        case _:
            pass

# Create needed objects
enemies = []
enemies.append(Enemy("slime", 1, 0.5, 1, 1))
enemies.append(Enemy("skeleton", 1.5, 1, 1, 2))
enemies.append(Enemy("ghost", 2, 2, 2, 5))
villager = (Enemy("villager", 3, 3, 3, 10))

dungeons: list[Dungeon] = []
dungeons.append(Dungeon("Moss Grotto (easy)", random.randrange(2, 3), 1, 8))
dungeons.append(Dungeon("Withered Catacombs (tough)", random.randrange(3, 5), 4,  12))
dungeons.append(Dungeon("Fiery Hollows (arduous)", random.randrange(4, 6), 10, 16))
dungeons.append(Dungeon("...Village.. what are you doing?? (insane)", 10, 14, 32))

specialTiles: list[SpecialTile] = []
specialTiles.append(SpecialTile("=", True, False))
specialTiles.append(SpecialTile("=", True, True))
specialTiles.append(SpecialTile("-", False))

player = Player(usrname, 1, 0, 5, 5, 1, 1, 1)
curEnemy: Enemy = None
village = Village(60)

# main program

print(f"Hello {usrname}, age {age} !")
if age > 120:
    time.sleep(1)
    print("Wow.. you're *really* old !")
    time.sleep(1)
print("")
print("You find yourself in a mysterious world of Aequitas")
print("Surrounded by vast fields and forests, remembering you were entrusted to save the village")
print("Along your travels, you notice entrences embedded in the ground, unsaitiably curious, you are compelled inward")
print("However, this isnt the first one you've seen, not even the second, but the third !")
print("In this world, the choice is yours, what is it you'd like to do?")

while True:
    DisplayOptions()