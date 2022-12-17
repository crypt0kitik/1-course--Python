# TASK: there is a list of dictionaries
# divide the movies into two lists
# print lists

# dict
movies = [
    {"name" : "Casablanca",
    "year": 1942},
    {"name" : "Forrest Gump",
    "year": 1994},
    {"name" : "Avatar",
    "year": 2009},
    {"name" : "Schindler's List",
    "year": 1993},
    {"name" : "Fight Club",
    "year": 1999},
    {"name" : "The Matrix ",
    "year": 1999},

]

# for creating new lists
mov_before_2000 = []
mov_after_2000 = []

# loop for checking the movie year
for movie in movies:
    year = movie["year"]
    name = movie["name"]
    if year < 2000:
        mov_before_2000.append(name)
    else:
        mov_after_2000.append(name)

# print results
print(f"These movies have been released in year 2000 or later:" , ', '.join(mov_after_2000))
print()
print(f"These movies have been released before the year 2000:" , ', '.join(mov_before_2000))