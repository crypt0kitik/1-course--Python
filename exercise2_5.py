# need to import a module and generate a random value
import random
guess = random.randint(1, 10)
print(guess)

# generate length of sides of a rectangle
side_1 = random.randint(2, 10)
side_2 = random.randint(2, 10)
print(f"First random side: {side_1}")
print(f"Second random side: {side_2}")

# calculate area of the rectangle
area = side_1 * side_2

# show results
print(f"Rectangle area: {area}")