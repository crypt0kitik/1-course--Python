# task: ask from the user 5 positive integers
# and print only the biggest number

# for creating a list
number_list = []

# ask in the loop from the user 5 positive integers
for number in range(5):
    number = input("Give a number:\n")
    number = int(number)
    # create a list
    number_list.append(number)
    if number <= 0:
        print("Not correct format!")
        break

# sort the list, where the last is biggest
number_list.sort()
# print the results
print("The biggest number from the user:", number_list[-1])