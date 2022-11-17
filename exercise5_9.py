# task: use list comprehension feature
# there is a list, which contains at least 10 name
#  Use list comprehension, and print only those names
#  that follow all these conditions at the same time:
# 1. Names that do not contain the letter "s"
# 2. Names that do not contain the letter "e"
# 3. Names that are less than 8 characters long
# 4. Names that contain a maximum of 2 vowels

# list, which contains at least 10 different names
name_list = ["Pekka", "Pelageia", "Angelina", "Susanna", "Emiliia",
             "Larisa", "Alina", "Aleksei", "Vladislav", "Mario",
             "RedBull", "Ekaterina", "Loli", "Pepi", "Niko"]

new_list = []
vowels = "AEIOUaeiou"

# make a loop to work with all names
for name in name_list:
    # split names to letters
    letters = [letter for letter in name]
    name_length = len(name)
    # check if names contain letters "s" and "e"
    if "s" not in name and "e" not in name:
        # check if names are less than 8 characters long
        if name_length < 8:
            count = list(map(name.count, "AEIOUaeiou"))
            if sum(count) <= 2:
                new_list.append(name)

# print the result: new list with names
print(new_list)