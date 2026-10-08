usri = None
smi = usri #storage min
sma = usri #storage max

print("Input a bunch of numbers, when you input nothing program quits")
print("When you wanna quit, ill show youthe highest and lowest of what you put in")

def getNums(txt):
    global sma
    global smi
    global usri
    try: usri = int(input(txt))
    except:
        usri = None
        print("something went wrong") #Doesn't output
    if usri != None:
        if sma == None or usri > sma:
            sma = usri
        if smi == None or usri < smi:
            smi = usri

getNums("Input a whole number: ")

#print(f"useri = {usri}")

while usri != None:
    getNums("Input your next whole number: ")

print(f"smallest number was {smi}, and largest was {sma}")