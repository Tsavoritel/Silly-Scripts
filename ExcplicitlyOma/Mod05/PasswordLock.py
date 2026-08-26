attempts = 5
cru = "python"
crp = "rules"
print("Please input credientials")
while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")
    attempts -= 1
    if username == cru and password == crp:
        print("Welcome")
        attempts = -1
    else: print(f"{attempts} attempts remaining.")
if attempts == 0: print("Access denied")
#TEST