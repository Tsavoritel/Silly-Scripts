listOfFullNums = []
listOfOddsNums = []
def addToList():
    for i in range(5):
        try:
            thisnum = int(input("Please input a number: "))
        except:
            print("Invalid input.")
            return
        listOfFullNums.append(thisnum)
        if thisnum % 2 == 0:
            listOfOddsNums.append(thisnum)
addToList()
print(f"The total of the numbers is {sum(listOfFullNums)}")
print(f"The total of the even numbers is {sum(listOfOddsNums)}")
