# import module to make sqrt
from math import sqrt

# ask the sides
side_1 = input("Give me the first side: \n")
side_1 = float(side_1)
side_2 = input("Give me the second side: \n")
side_2 = float(side_2)

# make calculations
hypotenuse = sqrt(side_1**2 + side_2**2)
hypotenuse = round(hypotenuse, 2)

# show the results
print(f"The length of the hypotenuse is: {hypotenuse} m")
