import random
randmin = 1
randmax = 20
rand = int(random.randint(1, 20))

cd = 3 #"close delta" or how far away should the program consider a number to be close
answerrange = range(rand-cd, rand+cd)
hint = ""

guesscnt = 0
usrguess = 0

print(f"A random number was generated (1-{randmax})")

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
        yourrange = range(usrg-cd, usrg+cd)
        if range(max(yourrange[0], answerrange[0]), min(yourrange[-1], answerrange[-1])+1):
            hint = "you are close !!"
        else:
            hint = "you are far away..."
        print(f"You guessed wrongly {guesscnt} time(s) !!")
        print(f"Hint... {hint}")
        guess()
guess()