# TASK: create an application that produces safe passwords
# ask a password length from the user
# don't accept passwords less than 8 characters
# create a new password (by using a loop) of the desired length
# a) The password has to have at least one lower letter
# b) The password has to have at least one CAPITAL letter
# c) The password has to have at least one number
# d) The password has to have at least one of the special characters: -_~?*$#!+%@

# import modules
# I use "secrets" because random numbers are really only pseudo-random
# the secrets module knows how to tap into operating system sources of randomness (called entropy)
import secrets
import string

# string constants from module "string"
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


length = True

while length:
    # ask for length from the user
    length = input("What length of a password you want? \n")
    length = int(length)

    # continue to ask until you get 8 or more characters
    if length < 8:
        print("The password length should be at least 8 characters.")
        print("Write length again!")
        print()

    # when you get 8 or more characters, create a password
    elif length >= 8:
        password = ''.join(secrets.choice(lower + upper + num + symbols) for t in range(length))
        print(f"Your new safe password is ready: {password}")
        length = False

