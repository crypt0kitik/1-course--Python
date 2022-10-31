# ask for money in the first time
money = input("Give money: \n")
money = float(money)

purchase_cost = input("Purchase cost: \n")
purchase_cost = float(purchase_cost)

# check if there is enough
if money >= purchase_cost:
    change = money - purchase_cost
    print(f"Thank you. Here's the change: {change}")

# if there is not enough, ask again and count change
else:
    money <= purchase_cost
    new_money = input("Not enough money, give more: \n")
    new_money = float(new_money)

    if new_money >= purchase_cost:
        change = new_money - purchase_cost
        print(f"Thank you. Here's the change: {change}")
    else:
        print("You don't have enough money.")
