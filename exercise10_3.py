# TASK: application that gives the user
# a random proverb from the file

# import random module to make random proverb
import random

# open the file to read
file_handle = open("wisewords.txt", "r")

# read all contents to a variable
# and create a list from file
content = file_handle.read()
proverbs_list = content.split("\n")

# make random choice from the list
proverb = random.choice(proverbs_list)

# print results
print("Today's proverb:")
print(proverb)

# close the connection in the end
# to avoid strange file locking bugs
file_handle.close()