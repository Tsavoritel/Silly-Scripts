import math
def MakePeri():
    w = None
    l = None
    a = None
    try:
        w = int(input("What is the width of the rectangle ? "))
        l = int(input("...and the length ? "))
    except:
        print("You need to input a number !!")
        MakePeri()
    if (w != None):
        p = 2*(w+l)
        a = l*w
        print(f"The perimeter of your rectangle is: {p}\n...and the area is: {a}")
MakePeri()