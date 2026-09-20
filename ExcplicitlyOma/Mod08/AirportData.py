airports = {"EFHK": "Helsinki-Vantaa", "KIAG": "Niagara Falls", "NFFN": "Nadi"}
useri = "-"
while useri != "":    
    print("Options: enter a new airport (e), fetch the information of an existing airport (f) or quit (q)")
    useri = input("Input: ")
    match useri:
        case "e":
            k = input("Enter 4 digit ICAO code: ")
            v = input("Enter the name of the airport: ")
            airports.update({k: v})
        case "f":
            icao = input("What ICAO code would you like to lookup? ")
            if icao in airports:
                print(f"The corresponding airport is: {airports.get(icao)}")
            else:
                print("ICAO not yet in dictionary !")
        case "q":
            exit
        case _:
            print("Invalid input !")