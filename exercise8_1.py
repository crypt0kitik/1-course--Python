# TASK: create an application that asks the user
# to provide the birth years, save it
# after this, determine each person's age

# import modules
from datetime import date
from colorama import Fore, Back, Style

# asks the user to provide the birth years
count = 1
years_list = []

# date for counting age
today = date.today()

# loop for user input
while count < 6:
    birth_year = int(input(f"Give the birth year of person {count}: \n"))
    count = count + 1
    years_list.append(birth_year)

print("Let's process all birth years...")
print()

# results about ages
for birth_year in years_list:
    age = today.year - birth_year
    if 0 <= age <= 125:
       print(Fore.GREEN + f"{age} years old, age OK!")
       Style.RESET_ALL
    else:
       print(Fore.RED + f"{age} years old, incorrect age.")
       Style.RESET_ALL

print("All done!")
