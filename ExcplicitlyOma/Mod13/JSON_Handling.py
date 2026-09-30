import json

save_data = {
    "player": "elebebeeee",
    "items": ["ball", "sword"]
}

movie_data = {
    "Name": "Somewhere in Time",
    "Year": "1980",
    "Actors": [ "Christopher Reeve", "Jane Seymour" ]
}

with open("ExcplicitlyOma/Mod13/savedata.json", "w") as save_file:
    json.dump(save_data, save_file)
with open("ExcplicitlyOma/Mod13/savedata.json", "r") as save_file:
    save_file_data = json.load(save_file)
    print(save_file_data)

with open("ExcplicitlyOma/Mod13/moviedata.json", "w") as movie_file:
    json.dump(movie_data, movie_file)
with open("ExcplicitlyOma/Mod13/moviedata.json", "r") as movie_file:
    movie_file_data = json.load(movie_file)
    print(movie_file_data)