import random
rand = int(random.randint(1, 10))
guesscnt = 0
usrguess = 0
test = False

def guess():
    try:
        usrguess = int(input("give a random number as a guess "))
    except:
        print("give an actual number please !")
        guess()
    test = usrguess == rand
    # print(f"rand: {rand} = {usrguess} is {test}")
    processguess(usrguess)

def processguess(usrg):
    global guesscnt
    if (usrg == rand):  
        print("congrats !!")
        print(guesscnt)
        exit
    else:
        guesscnt += 1
        print(f"you lost {guesscnt} times !!")
        guess()
guess()