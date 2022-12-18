# TASK: Create a function called magazine_serial_check(serial)
# that takes only one parameter as a text:
# the ISSN-serial


# import functions from the file
from functions import *

user_data = input("Give an ISSN-serial: \n")

# run the function
result = magazine_serial_check(user_data)

# print results
if result:
    print("Valid ISSN.")
else:
    print("Incorrect ISSN.")