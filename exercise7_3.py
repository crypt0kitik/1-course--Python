# TASK: there is a dictionary
# print the receipt of all purchases in a loop

# dictionary
shopcart = [
    {"name": "Beehive - lamp", "price": 999.9},
    {"name": "Malm - bed", "price": 169.9},
    {"name": "Moomin - mug set", "price": 59.9},
    {"name": "Nemo - divan", "price": 699.9},
    {"name": "Ritz - armchair", "price": 369.9}
]

# variables for calculation
total_price = 0
total_vat = 0
print("Receipt:")

# give variables to ele in list
for product in shopcart:
    name = product['name']
    price = product['price']

    # print name and price of one product
    print(f"- {name}")

    # calculate total price
    total_price = total_price + price

    # calculate total vat
    vat_product = price / 1.24
    vat_product = round(vat_product, 1)
    vat = price - vat_product
    total_vat = total_vat + vat
    total_vat = round(total_vat, 1)

# print results
print()
print(f"Total sum: {total_price}")
print(f"Total vat: {total_vat} €.")
print("Please come again!")