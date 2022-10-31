# ask for the year
year = input("Give year: \n")
year = int(year)

# modulo operator % to check if the year is divided by 4 without remainder
# modulo operator % to check if the year is divided by 100 with a remainder
# modulo operator % to check if the year is divided by 400 without remainder
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year: YES")
# otherwise, print Leap year: NO
else:
    print("Leap year: NO")