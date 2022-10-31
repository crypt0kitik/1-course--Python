# import math module to round weight
import math

# is it a letter or a parcel
item = input("Is it a letter or a parcel? Write l or p: \n")

# what is a weight of the shipment
weight = input("What is a weight of the shipment? \n")
weight = int(weight)

# base cost letter - 50 cents, parcel - 2 euro
if item == "l" and weight <= 200:
    print("Your shipment cost for letter is 50 cents.")

if item == "p" and weight <= 200:
    print("Your shipment cost for the parcel is 2 euro.")

# extra weight letter - 200-500g is 4 cent per 100g, more 500g is 7 cent per 100g
# delivery are measured by full 100 grams, 499 is 400
if item == "l" and 200 < weight < 500:
    weight = weight / 100
    weight = math.floor(weight)
    cost = (weight * 4) + 50
    print(f"Your shipment cost for letter is {cost} cents.")
elif item == "l" and weight > 500:
    mailbox = input("Does your letter fit the mailbox? y/n: \n")
    if mailbox == "y":
        weight = weight / 100
        weight = math.floor(weight)
        cost = (weight * 7) + 50
        print(f"Your shipment cost for letter is {cost} cents.")
    else: # if letter is more than 500g, add an extra 2 € to the price
        weight = weight / 100
        weight = math.floor(weight)
        cost = (weight * 7) + 50 + 200
        print(f"Your shipment cost for letter is {cost} cents.")

# extra weight parcel - 200-500g is 8 cent per 100g, more 500g is 14 cent per 100g
if item == "p" and 200 < weight < 500:
    weight = weight / 100
    weight = math.floor(weight)
    cost = (weight * 8) + 200
    print(f"Your shipment cost for parcel is {cost} cents.")
elif item == "p" and weight > 500:
    weight = weight / 100
    weight = math.floor(weight)
    cost = (weight * 14) + 200
    print(f"Your shipment cost for parcel is {cost} cents.")