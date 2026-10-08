import math
def checkYear():
    year = int(input("What year do you want to check: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        print("It is a leap year!")
    else:
        print("Not a leap year!")
    q = input("Would you like to check another? (y/n): ")
    if q == "y":
        checkYear()
checkYear()