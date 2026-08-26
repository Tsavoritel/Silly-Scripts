usri_1 = None
usri_2 = None
fa = None
mod = None

def runCalc():
    global fa
    match mod:
        case "+":
            fa = usri_1 + usri_2
        case "-":
            fa = usri_1 - usri_2
        case "m":
            fa = usri_1 * usri_2
        case "q":
            print("Quitting...")
        case _:
            mod = "bad"
            print("Invalid input !")
    if fa != None and mod != "bad":
        print(f"The result of your calculation is: {fa}")

print("Welcome to SimpleTermCalc")
while mod != "q":
    try:
        usri_1 = int(input("x="))
        mod = input("Options: +, -, m (multiply), q (quit): ")
        try:
            usri_2 = int(input("y="))
            runCalc()
        except: print("Invalid input !")
    except: print("Invalid input !")
