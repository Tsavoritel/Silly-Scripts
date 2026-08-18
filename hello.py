import random
rand = random.randint(1, 10)
guess = int(input("give a random number as a guess "))
if guess == rand:
    print("congrats !!")
else:
    print("you stink !!")