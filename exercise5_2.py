# create a variable average
average = 0

# ask the user for 12 times the rain amount of the month
for x in range(12):
    number = int(input("Give the rain amount of the month:\n"))
    average = average + number

# calculate the average
average = average / 12
# print the final result
print(average)

