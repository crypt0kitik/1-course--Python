# TASK: create a function that generates
# a random series of lottery numbers,that
# contains 7 unique numbers between 1 and 40

# creating function in the file
# because there is no other space
# for the task submission
def lottery_numbers():
    import random
    collecton = []
    loop = 0
    while loop < 7:
        number = random.randint(1, 40)
        if number in collecton:
            continue
        else:
            collecton.append(number)
            loop = loop + 1
    return collecton

# generate lottery numbers
# by running the function
lottery_number = lottery_numbers()

# print lottery numbers
print("Here you can find lottery numbers:")
print(' '.join(map(str, lottery_number)))
