#mod01 excercise1, mod02 excercise2, and project 1-3

name = input("Enter your name: ")
uin = ""
items = []

#age check

try:
    age = int(input("...and your age? "))
except:
    print("Please input a whole number.")
if age < 13:
    print("You are a minor, and are not yet old enough to use this product")
    print("Shutting down...")
    exit

#main program

def ItemAdder(item):
    items.append(item)
def CheckInventory():
    print(items)
def PlayerInfo():
    print(f"You are {name} and are {age} years old.")

print(f"Hello {name}, age {age} !")
while uin != "lopeta":
    print("Options: gotitem, inventory, whoami, lopeta")
    uin = input("Input: ")
    match uin:
        case "gotitem":
            ItemAdder(input("What item did you pickup? "))
        case "inventory":
            CheckInventory()
        case "whoami":
            PlayerInfo()
        case "lopeta":
            print("Exiting...")
        case _:
            print("Invalid option, please choose from the following list")
