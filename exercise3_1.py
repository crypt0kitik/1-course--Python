# ask data
number_1 = input("Write the first number: \n")
number_1 = int(number_1)

number_2 = input("Write the second number: \n")
number_2 = int(number_2)

# compare numbers
if number_1 > number_2:
    print(f"The bigger number is: {number_1}")
elif number_1 < number_2:
    print(f"The bigger number is: {number_2}")

if number_1 == number_2:
    print("Numbers are equal")
