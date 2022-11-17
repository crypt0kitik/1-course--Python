# TASK: ask info about status, sales codes and VIP points from user
# count price for parcel or letter
# print results

# inputs here, ask the order cost €
# is the user a student
# is the user a VIP
# ask for the sales code
cost = input("What is your total cost of the order (€)? \n")
cost = float(cost)
student = input("Are you a student? y/n: \n")
vip = input("Are you VIP? y/n: \n")
code = input("Do you have a sales code? If yes, write it here: ")

# if FALL22
    # total cost is total cost * 0.1 (10% discount)
if code == "FALL22":
    total_cost = cost -(cost * 0.1)
# elif BK2SCHOOL and user is a student
    # total cost is total cost * 0.2 (20% discount)
elif code == "BK2SCHOOL" and student == "y":
    total_cost = cost - (cost * 0.2)
else:
    pass

# if VIP:
    #  ask the user how many VIP points the user has from previous purchase
    # calculate how many points VIP has now
    # for each whole 10€ in the total cost, give the user 100 new VIP points
    # reduce the total cost by 5€ for each full 1000 VIP points
if vip == "y":
    previous_points = input("How many VIP points you have from the previous purchase? \n")
    previous_points = int(previous_points)
    points = cost / 10
    points = round(points, 0)
    new_points = points * 100
    total_points = previous_points + new_points
    reduction = total_points / 1000
    reduction = round(reduction, 0)
    reduction = reduction * 5
    total_cost = total_cost - reduction

# if total cost < 99
    # add shipment costs 7.95€
    # print total cost

if total_cost < 99:
    total_cost = total_cost + 7.95
    print(f"You have to pay for shipment. You total cost is {total_cost} euro.")
else:
    print(f"You do not need to pay for shipment. You total cost is {total_cost} euro.")