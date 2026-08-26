print("These are all the numbers divisible by 3 between 1-1000: ")
num = 0
numbers = ""
totaln = 0
while num <= 1000:
    num += 1
    if num % 3 == 0:
        numbers += f"{num}, "
        totaln += 1
    if num % 24 == 0:
        numbers += "\n"
print(numbers)
print(f"total numbers: {totaln}")