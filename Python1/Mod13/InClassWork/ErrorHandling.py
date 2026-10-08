import os

file = input("What file do you wanna read? ")

try:
    with open(f"ExcplicitlyOma/Mod13/{file}") as my_file:
        file_data = my_file.read()
except FileNotFoundError as e:
    print("Error: File not found")
    print(e)