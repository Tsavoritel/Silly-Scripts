names = {""}
potnewname = "-"
while potnewname != "":
    potnewname = input("Enter a name: ")
    if potnewname == "":
        exit
    elif potnewname in names:
        print("Name already exists")
    else:
        print("New name !")
        names.add(potnewname)
names.remove("")
print(names)