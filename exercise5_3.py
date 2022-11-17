# import pi for calculation of area
import math
from math import pi

running = True

# while running variable == True
while running:

    # ask radius of a circle, calculates the area and print the result
    radius = input("Give radius:\n")
    radius = float(radius)
    area = pi * radius ** 2
    area = round(area, 2)
    print(f"Circle area: {area}\n")

    # ask user if they want to continue the application
    answer = input("DO you want to ontinue? (y/n):\n")

    # if user answers "n", quit the application
    # (break out from the while-loop)
    if answer == "n":
        running = False