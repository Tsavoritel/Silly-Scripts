seasons = ("spring", "summer", "autumn", "winter")
month = int(input("What month would you like to check the season of: "))
if month == 12 or month in range(1, 2):
    print(seasons[3])
elif month in range (3, 5):
    print(seasons[0])
elif month in range (6, 8):
    print(seasons[1])
elif month in range (9, 11):
    print(seasons[2])