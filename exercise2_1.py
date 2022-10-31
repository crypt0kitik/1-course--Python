# import math module to use pi in calculations
import math

# ask data of sides
side_1 = input("Give the first side:\n")
side_1 = float(side_1)
side_2 = input("Give the second side: \n")
side_2 = float(side_2)
side_3 = input("Give the third side: \n")
side_3 = float(side_3)

# calculate the volume of the box
volume = side_1 * side_2 * side_3
print(f"Volume of the box is: {volume} m3")

# the radius of a sphere in decimal and calculate the volume of the sphere (V)
radius = input("Give the sphere radius: \n")
radius = float(radius)

volume = (4/3) * math.pi * radius ** 3
volume = round(volume, 2)
print(f"Sphere volume is: {volume}")