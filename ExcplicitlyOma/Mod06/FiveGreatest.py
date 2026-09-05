import copy
uinput = ""
numbers = [11 , 22, 33, 44, 55, 66, 77]
#while uinput != "null":
#    try:
#        uinput = int(input("input any number: "))
#        numbers.append(uinput)
#    except:
#        uinput = "null"
print(f"debug1: {numbers}")
snum = copy.copy(numbers.sort(reverse=True))
print(f"debug2: {snum}")
for i in numbers:
    try:
        snum.pop(5)
    except:
        print(snum)
#howwwwwwwwwwwwww