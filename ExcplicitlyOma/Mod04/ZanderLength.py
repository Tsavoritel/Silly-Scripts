print("Hey, I really need a big zander, think you can find one?")
idealleng = 42
caughtleng = int(input("(What was the length of the fishy you caught?): "))
if caughtleng >= idealleng:
    print("Yay thats large enough !!")
else:
    print(f"Oof, sorry I need something thats at least {idealleng - caughtleng} centimeter(s) longer !")