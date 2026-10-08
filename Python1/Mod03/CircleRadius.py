import math

def makerad():
    # I realize this might be somewhat overengineered but I like adding exceptions
    try:
        rad = int(input("What is the radius of your circle ? "))
    except:
        print("Needs to be a number !!")
        makerad()
    print(f"The area of your cirlce is: {round(math.pi * pow(rad, 2), 1)}")
makerad()