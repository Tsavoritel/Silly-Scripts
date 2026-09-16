import random
roll = -1
try:
    maxSides = int(input("How many sides should the die have? "))
except:
    print("Invalid input.")
def RollDieUntil6(maxs):
    global roll
    roll = random.randrange(1, maxs+1)
    print(f"This roll: {roll}")
while roll != maxSides:
    RollDieUntil6(maxSides)
print(f"Final roll: {roll}")