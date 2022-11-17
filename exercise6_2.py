# task: application allows the user to print
# the chosen multiplication table in the range of 1-10

while True:
    # ask from the user a number in the range of 1-10
    number = input("Which multiplication table you want to see? (0-10). 0 stops program.\n")
    number = int(number)
    # check if the number in the correct range
    if 1 <= number <= 10:
        # make a multiplication table
        for i in range(1, 11):
            print(number, 'x', i, '=', number * i)
    # if number is bigger 10, ask number again
    elif number < 0 or number > 10:
        print("Wrong number format")
        continue
    # if the user inputs "0" (zero), stop the application
    elif number == 0:
        print("You stop the program")
        break
