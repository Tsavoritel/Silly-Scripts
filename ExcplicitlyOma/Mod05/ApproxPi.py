import math
import random

x = []
y = []

maxn = int(input("How many points to generate? ")) # N
# maxh = int(input("Max random number to generate? "))

n = 0 # n thats in circle A
c = 0 # counter

while (c < maxn):
    px = random.random() #points in unknown square
    py = random.random()#1, maxh)
    if math.pow(px, 2)+math.pow(py, 2) < 1: #is it in the circle also?
        x.append(px)
        y.append(py)
        n += 1
    c += 1
    if c % (maxn / 100) == 0:
        percent = (c / maxn) * 100
        print(f"Loading: {round(percent)}%")

mypi = 4 * (n/maxn)
print(f"pi = {round(mypi, 20)}")