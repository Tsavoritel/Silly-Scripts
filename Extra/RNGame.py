import random
randmin = 1
randmax = 50
rand = int(random.randint(randmin, randmax))

hd = 3 #"hot delta" or how far away should the program consider a number to be close
wd = 12 #warm delta
answerhotrange = range(rand-hd, rand+hd)
answerwarmrange = range(rand-wd, rand+wd)
hint = ""

guesscnt = 0
usrguess = 0

print(f"A random number was generated ({randmin}-{randmax})")

def guess():
    try:
        usrguess = int(input("Input your guess: "))
    except:
        print("Give an actual number please !")
        guess()
    processguess(usrguess)

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