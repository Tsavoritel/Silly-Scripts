print("You musn't input a negative number...")
usri = 0
while usri >= 0:
    usri = int(input("Please provide inches to be converted into cm: "))
    print(f"That is equivalent to {round(usri * 2.45, 1)}cm")
print("You hath provided forbidden text, no more...")