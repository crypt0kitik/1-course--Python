# TASK: An application that determines which city in Finland
# has statistically the most warnings of slippery weather conditions
# print also the latest 5 slippery weather warnings
# based on the timestamp (city + date + time).

# import modules
import json
import requests
import var_dump as vd

# data from the Internet
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = requests.get(url)
data = req.json()

cities = []
most_warnings_city = ""


for item in data:
    city = item["city"]
    whole_date = item["updated_at"]
    cities.append(city)

# funciton to find most frequent
# element in a list
def most_frequent(cities):
    return max(set(cities), key = cities.count)

print(f"The city has more warnings than others:" , most_frequent(cities))

# Print also the latest 5 slippery weather
# warnings based on the timestamp (city + date + time)
print()
print("The latest 5 slippery weather warnings:")
print()

data.sort(key = lambda i: i['updated_at'], reverse = True)
for index in range(5):
    print('City Name: ', data[index]['city'])
    print('Create Time and date: ', data[index]['created_at'])
    print('Update Time and Date: ', data[index]['updated_at'])
    print()