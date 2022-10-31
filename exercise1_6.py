# ask to input data
money = input("Please enter the amount of money in cents (1-100): \n")
money = int(money)

# make calculations with "modulo operator" and print results
print(f"Amount of 50 cents: {money//50}")
money = money % 50
print(f"Amount of 20 cents: {money//20}")
money = money % 20
print(f"Amount  of 10 cents: {money//10}")
money = money % 10
print(f"Amount of 5 cents: {money//5}")
money = money % 5
print(f"Amount of 2 cents: {money//2}")
money = money % 2
print(f"Amount of 1 cent: {money}")
