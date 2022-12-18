# TASK: create a function:
# count_seconds(hours,minutes,seconds)

# import functions from the file
from functions import *

# ask for input
hours = int(input("Give hours:\n"))
minutes = int(input("Give minutes:\n"))
seconds = int(input("Give seconds:\n"))

# run the function
result = count_seconds(hours, minutes, seconds)
print(f"{result} seconds in total.")