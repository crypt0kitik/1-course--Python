# ask student y/n
# ask number of the month to travel
user = input("Are you a student? y/n: \n")
user = user.lower()

# The user is entitled to a special price, if they are a student (y)
# and the reservation is not on months 6 - 8
# if not, special_price –> variable to False

special_price = False

if user == "y":
    month = input("Travel month? (1-12): \n")
    month = int(month)
    if 1 <= month <= 5 or 9 <= month <= 12:
        # if a user gets a special price, special_price –> variable to True
        special_price = True

# print normal or special price
if special_price:
    print("Special price!")
else:
    print("Normal price.")