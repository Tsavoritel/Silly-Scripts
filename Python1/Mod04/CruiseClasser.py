print("Which class would you like to learn about?")
print("Options: LUX, A, B, C")

def findOption():
    cclass = input("Input: ")
    if cclass == "LUX":
        print("You will get a luxurious upper-deck cabin with a balcony.")
    elif cclass == "A":
        print("In A-class, you will find nice cabin above the car deck, equipped with a window.")
    elif cclass == "B":
        print("B-class has a windowless cabin above the car deck")
    elif cclass == "C":
        print("Our lowest class C, has windowless cabin above the car deck")
    else:
        print("Invalid cabin class. Please input a valid option !")
        findOption()
findOption()