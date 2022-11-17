# create a tuple of months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December")

# ask data from user
choice = input("Give the number of month: \n")
choice = int(choice)
choice = choice - 1 # because collections start from 0

# print number of a month
m = months[choice]
print(m)