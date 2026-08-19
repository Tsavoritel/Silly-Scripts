import random
rand = random.randint(1, 10)
guesscnt = 1
usrguess = int(input("give a random number as a guess "))

def guess():
    if usrguess == rand:  
        print("congrats !!")
    else:
        guesscnt += 1
        print(f"you stunk {guesscnt} times !!")
guess()