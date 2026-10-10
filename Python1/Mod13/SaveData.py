import json
import os

class player:
    def __init__(self, name):
        self.name = name
with open("Python1/Mod13/instructions.txt", "r") as file:
    instructions = file.read()
    print(instructions)

name = input("What is your name:")
player1 = player(name)

with open("Python1/Mod13/intro.txt", "r") as file:
    intro = file.read()
    print(intro)

if os.path.exists("Python1/Mod13/save.json"):
    with open("Python1/Mod13/save.json", "r") as file:
        data_read = json.load(file)
        print(f"welcome back {data_read}")
else:
    with open("Python1/Mod13/save.json", "w") as file:
        json.dump(player1.name, file)
        print(f"hello {name}")