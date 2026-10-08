nhbm = range(134, 167)
nhbf = range(117, 155)
lowtxt = "Oh, it's a bit low"
hightxt = "Oh, it's a bit high"
print("Hey there, lets check your hemoglobin value (g/l)")
hb = int(input("What is your current readout? "))

def findStatus():
    g = input("..And were you born male or female? (m/f): ")
    if g == "f":
        if hb in nhbf:
            print("Okay, great, you're in a normal range")
        elif hb > max(nhbf):
            print(hightxt)
        elif hb < min(nhbf):
            print(lowtxt)
    elif g == "m":
        if hb in nhbm:
            print("Okay, great, you're in a normal range")
        elif hb > max(nhbm):
            print(hightxt)
        elif hb < min(nhbm):
            print(lowtxt)
    else:
        print("Please input an available option")
        findStatus()
findStatus()