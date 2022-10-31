# import math module to count apple
import math

# count cherry, apple
cherry = (2 + (2 * 2) + 2 - 2 - 2)/2
apple = math.sqrt(3 + 10 - 4) / 3
apple = apple + (5 ** 3 - 5) / 20
apple = apple + 3

# count orange, banana and pear
orange = apple - 9
banana = ((2 * cherry) - 10)/3
pear = (3 * banana) - 8

# make and print the last calculation
total = (apple - (2 * banana) + (2 * orange)) * (pear + cherry)
print(total)