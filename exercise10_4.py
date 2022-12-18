# TASK: download the file called ”countries.json”
# read the contents of the file into a variable,
# and print out the contents in a loop,
# one country in a row

# import module
import json

# open a file to read
# get the JSON data from the file
file_handle = open("countries.json", "r")
content = file_handle.read()

# convert JSON to Python data
cities = json.loads(content)

# cities is a list of dictionaries, so we can loop it:
print("All countries and capitals:")
for city in cities:
    print(f"{city['country']}: {city['capital']}")

# close the connection in the end
# to avoid strange file locking bugs
file_handle.close()
