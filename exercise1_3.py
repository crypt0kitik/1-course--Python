# Ask a length, make calculations and show the result

number = input("Give the length of the road in kilometers: ")
number = float(number)
number = number * 6.5 / 100
number = round(number, 1)
print(f"Fuel consumption: {number} l")