# task: ask the user for a year
# and only print those order codes from the list
# that have the matching year

# product identifiers list
# formula of product is "ORDERCODE_YEAR"
products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y82018_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

# ask the user for a year
year_from_user = input("Search codes for which year?\n")

for order_code in products:
    # split products to parts
    order_code = order_code.split("_")
    if year_from_user == order_code[1]:
        # print those order codes from the list, that have the matching year
        print(order_code[0])
    else:
        pass