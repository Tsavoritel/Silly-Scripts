try:
    inputnum = int(input("Input any number: "))
except:
    print("It's gotta be a number...")
primenum = True

for i in range(2, inputnum):
    print(f"{inputnum} / {i} = {inputnum / i}")
    if int(inputnum) % i==0:
        print(f"{inputnum} is not a prime number....")
        break
    else:
        print("You've got a prime number on your hands !")