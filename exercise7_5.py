# TASK: an application that downloads
# the current weather data from the internet
# informs the user which city in Finland
# has the strongest and weakest wind at the moment
# also, find averages of areas

# import modules for the application
import json
import requests
import var_dump as vd

# data from the Internet
url = "https://edu.frostbit.fi/api/weather/"
req = requests.get(url)
data = req.json()

# variables for comparision
strongest_wind = 0
strongest_city = ""
weakest_wind = 0
weakest_city = ""

# variables for average
summary = 0
lapland_cities = []
south_cities = []
middle_cities = []


for item in data:
    wind = item["wind"]
    location = item["location"]
    area = item["area"]

    # fing the strongest wind
    if wind > strongest_wind:
        strongest_wind = wind
        if strongest_wind == wind:
            strongest_city = location

    # find the weakest wind
    if wind < weakest_wind or weakest_wind == 0:
        weakest_wind = wind
        if weakest_wind == wind:
            weakest_city = location

    # find average in areas
    if area == "lapland":
        lapland_cities.append(wind)
        lapland_average = sum(lapland_cities) / len(lapland_cities)
        lapland_average = round(lapland_average, 2)
    if area == "south":
        south_cities.append(wind)
        south_average = sum(south_cities) / len(south_cities)
        south_average = round(south_average, 2)
    if area == "middle":
        middle_cities.append(wind)
        middle_average = sum(middle_cities) / len(middle_cities)
        middle_average = round(middle_average, 2)


# print results
print(f"The strongest wind today at location: {strongest_city}, {strongest_wind} m/s")
print(f"The weakest today at location: {weakest_city}, {weakest_wind} m/s")
print()
print(f"Average wind, Lapland: {lapland_average}")
print(f"Average wind, Southern Finland: {south_average}")
print(f"Average wind, Middle part of Finland: {middle_average}")