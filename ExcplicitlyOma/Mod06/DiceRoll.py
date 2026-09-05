import random
total = 0
dieCount = int(input("How many dice would you like to roll? "))
for i in range(dieCount):
    total += random.randrange(1,6)
    print(f"This roll: {total}")

print(f"Total: {total}")