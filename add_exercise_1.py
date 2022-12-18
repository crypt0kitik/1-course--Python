# TASK: create a reminder app

# import time module
import time

# ask data from the user
user_reminder = input("What shall I remind you about? \n")
print()
local_time = float(input("In how many minutes?\n"))

# Python’s time.sleep() method requires seconds, not minutes
# I need to change to minutes
# calculate
local_time = local_time * 60
time.sleep(local_time)

# print results
print(user_reminder)
