# TASK: create a function called
# show_numbered_list(title, data)
# the function has to print the title text first,
# and then print a numbered list of all participants

# import functions from the file
from functions import *

# ask all the names as one string from user
people_string = input("Write all participants, separated by a comma:\n")
people = people_string.split(",")

# run the function and  print the list
# in original order
show_numbered_list("Original order:", people)

# sort the list into alphabetical order in your code,
# and print the list by using the function
people.sort()
show_numbered_list("Alphabetic order by first name:", people)


# sort the list into alphabetical order based on the surname
# print the list by using the function
people.sort(key=lambda x: x.split()[-1])
for i in range(len(people)):
    people[i] = ' '.join(reversed(people[i].split(' ')))

show_numbered_list("Alphabetic order by last name", people)

