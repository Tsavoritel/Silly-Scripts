import random
randmin = 1
randmax = None
randmaxe = 10 #easy
randmaxh = 50 #hard

print("Welcome to RNG-ame")
mode = input("Would you like to play on easy or hard? (e/h): ")
if mode == "h":
    randmax = randmaxh
elif mode == "e":
    randmax = randmaxe
else:
    print("Invalid gamemode, defaulting to easy...")
    randmax = randmaxe


rand = int(random.randint(randmin, randmax))

hd = 3 #"hot delta" or how far away should the program consider a number to be close
wd = 12 #warm delta
answerhotrange = range(rand-hd, rand+hd)
answerwarmrange = range(rand-wd, rand+wd)
hint = ""

guesscnt = 0
usrguess = 0

print(f"A random number was generated ({randmin}-{randmax})")
print("Options: integer (for guess), or q to quit")

def guess():
    global usrguess
    usrguess = input("Input: ")
    if usrguess == int:
        processguess(usrguess)
    elif usrguess == "q":
        exit
    else:
        print("Invalid input !")
        guess()

def processguess(usrg):
    global guesscnt
    guesscnt += 1
    if (usrg == rand):
        print(f"Got it !! You guessed {guesscnt} time(s) !!")
        exit
    else:
        yourrange = range(usrg-hd, usrg+hd)
        if usrg in answerhotrange:
            hint = "you are hot !!"
        elif usrg in answerwarmrange:
            hint = "you are warm."
        else:
            hint = "you are far away..."
        print(f"You guessed wrongly {guesscnt} time(s) !!")
        print(f"Hint... {hint}")
        guess()
guess()