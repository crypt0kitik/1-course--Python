# TASK: ask the user the current outside temperature
# and the humidity percentage
# print the given temperature

# ask the outside temperature
# ask the humidity percentage
temperature = input("What is the outside temperature? \n")
temperature = int(temperature)
humidity = input("What is the humidity percentage? \n")
humidity = int(humidity)

# variables are False
freezing = False
heatwave = False
raining = False
hailstorm = False

# conditions when variable become True
if humidity > 80 and temperature > - 20:
    raining = True

elif -20 < temperature < 0:
    freezing = True

elif temperature > 20:
    heatwave = True

elif humidity > 80 and temperature < -20:
    hailstorm = True

# check booleans
if heatwave and raining:
    print("It's damp and hot.")
elif freezing:
    print("It's freezing outside.")
elif heatwave:
    print("Heatwave! Remember to hydrate!")
elif raining:
    print("It's raining.")
elif hailstorm:
    print("There's a hailstorm, be careful!")