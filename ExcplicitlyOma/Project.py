#mod01 excercise1, mod02 excercise2, and project 1-2
name = input("Enter your name: ")
try:
    age = int(input("...and your age? "))
except:
    print("Please input a whole number.")
uin = ""
if age < 13:
    print("You are a minor, and are not yet old enough to use this product")
    print("Shutting down...")
    exit
else:
    print(f"Hello {name}, age {age} !") # space is intentional
    while uin != "lopeta":
        print("Options: yay, whoami, lopeta")
        uin = input("Input: ")
        match uin:
            case "yay":
                print("Yaayyyyyy!!!!!!!")
            case "whoami":
                print(f"You are {name} and are {age} years old.")
            case "lopeta":
                print("Exiting...")
            case _:
                print("Invalid option, please choose from the following list")
