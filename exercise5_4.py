# input varibales
list = ["Rome", "Athens", "Stockholm", "London", "Dublin", "Paris"]
# sort the list alphabetically
list.sort()

number = 0

# print the contents of the list by using a loop
for x in list:
    # create a count before the city
    number = number + 1
    print(f"{number}: {x}")

