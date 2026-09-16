import math
def ValueCalc(diameter, price):
    return price / (math.pi*math.pow(diameter/2, 2))

pizza1_d = int(input("What is the diameter of the first pizza: "))
pizza1_p = int(input("What is the price of the first pizza: "))
pizza2_d = int(input("What is the diameter of the second pizza: "))
pizza2_p = int(input("What is the price of the second pizza: "))

if ValueCalc(pizza1_d, pizza1_p) < ValueCalc(pizza2_d, pizza2_p):
    print("Pizza 1 is better value")
    print(f"Pizza 1 has a value of {ValueCalc(pizza1_d, pizza1_p)} euro per square meter")
else:
    print("Pizza 2 is better value")
    print(f"Pizza 2 has a value of {ValueCalc(pizza2_d, pizza2_p)} euro per square meter")