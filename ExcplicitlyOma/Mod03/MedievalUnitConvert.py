l = 13.3
p = 32*l
t = 20*p
def GetValues():
    unit = None 
    value = None
    #try:
    #    unit = ("lot", "talent", "pound")(input("What unit do you want to convert?\nOptions: talent, pound, or lot: "))
    #except:
    #    print("Not a valid unit !!")
    #    GetValues()
    unit = input("What unit do you want to convert?\nOptions: talent, pound, or lot: ")
    if(unit == "lot" or unit == "talent" or unit == "pound"):
        try:
            value = int(input(f"Please input how much mass in {unit}s: "))
            ConvertValue(unit, value)
        except:
            print("Not a number !!")
            GetValues()
    else: 
        print("Not a valid unit !!")
        GetValues()
def ConvertValue(u, v):
    fv = None #final value
    fu = "grams" #final unit
    match u:
        case "talent":
            fv = v*t
        case "pound":
            fv = v*p
        case "lot":
            fv = v*l
        case _:
            print("How did you get here")
    if fv > 999: #if its a kilogram call it as such
        fv /= 1000
        fu = "kilograms"
    print(f"{v} {u}s = {round(fv, 1)} {fu}")
GetValues()