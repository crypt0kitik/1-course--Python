try:
    # ask for data form user
    number_1 = input("First number: \n")
    number_2 = input("Second number: \n")

    # check if it is text or nor
    if number_1.isnumeric() and number_2.isnumeric():
        number_1 = float(number_1)
        number_2 = float(number_2)
        result = number_1 / number_2
        print(f"Result: {result}")
    else:
        print("Incorrect format.")

except ZeroDivisionError:
    print("You can't divide by zero!")