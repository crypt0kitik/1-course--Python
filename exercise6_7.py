# TASK: ask a range from the user
# find a number which is divisible by both 5 and 7

# ask the range from the user
range_start = input("Give the range start: ")
range_start = int(range_start)
range_end = input("Give the range end: ")
range_end = int(range_end)

# create a range
range = range(range_start, range_end)

for number in range:
    # check if number divided by 5 and 7
    if number % 5 == 0 and number % 7 == 0:
        print(f"The number {number} is divisible by both 5 and 7!")
        # stop the search immediately
        break
    # check if number divided by 5
    elif number % 5 != 0:
        print(f"{number} is not divisible by 5, skip")
    # check if number divided by 7
    elif number % 7 != 0:
        print(f"{number} is not divisible by 7, skip")

# check if the number is not founded
if number % 5 != 0 and number % 7 != 0:
    print("Suitable number is not found in the range!")