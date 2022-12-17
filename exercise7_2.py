# TASK: create list inventory
# print it using the loop

fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits + berries + vegetables]

for item in inventory:
    print(item)