import math
import random

maxn = int(input("How many points to generate? ")) # N

n = 0 # n thats in circle A
c = 0 # counter

while (c < maxn):
    px = random.random() #points in unknown square
    py = random.random()#1, maxh)
    c += 1
    if math.pow(px, 2)+math.pow(py, 2) < 1: #is it in the circle also?
        n += 1
    if c % (maxn / 100) == 0:
        percent = (c / maxn) * 100
        print(f"Loading: {round(percent)}%")

mypi = 4 * (n/maxn)
print(f"pi = {round(mypi, 20)}")