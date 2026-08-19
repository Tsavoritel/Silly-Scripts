import random
rand = random.randint(1, 10)
guesscnt = 0
wincon = False
usrguess = ""

def guess():
    usrguess = int(input("give a random number as a guess "))
    processguess()

def processguess():
    global guesscnt
    if usrguess == rand:  
        print("congrats !!")
        print(guesscnt)
    else:
        guesscnt += 1
        print(f"you lost {guesscnt} times !!")
        print(guesscnt)
        guess()

guess()
# while wincon == False: