with open("ExcplicitlyOma/Mod13/shopping.txt", "w") as file:
    file.write("milk\nbread\neggs")

with open("ExcplicitlyOma/Mod13/shopping.txt", "a") as file:
    file.write("\napples")

with open("ExcplicitlyOma/Mod13/shopping.txt", "r") as file:
    file_data = file.readlines()
    line_length = len(file_data)
    print(file_data)
    print(f"Items on the list: {line_length}")
