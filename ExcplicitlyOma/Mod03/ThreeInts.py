import math
def GetValues():
    num1 = None
    num2 = None
    num3 = None
    print("Please input 3 numbers:")
    try:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        num3 = int(input("Number 3: "))
        ManipulateValues(num1, num2, num3)
    except:
        print("That wasn't a number !!")
        GetValues()
    return num1, num2, num3
def ManipulateValues(n1, n2, n3):
    s = n1+n2+n3
    p = n1*n2*n3
    a = (n1+n2+n3)/3
    print(f"\nAnswers:\nSum = {s}\nProduct = {p}\nAverage = {a}")
GetValues()