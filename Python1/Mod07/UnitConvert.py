litersInGallon = 3.785411784
def Convert():
    global litersInGallon
    try:
        gallons = int(input("How many gallons? "))
    except:
        print("Invalid input.")
    if gallons > 0:
        print(f"{gallons} gallons is equal to {round((gallons*litersInGallon), 2)} liters.")
        Convert()
    else:
        print("Exiting...")
        return
Convert()