# Ask VAT, make calculations and show the result

number = input("Give the price without VAT: ")
number = float(number)
number = number * 1.24
number = round(number, 2)
print(f"Price with VAT: {number} €")