# TASK: there is a collection of 6 restaurants
# ask questions from the user
# create a list, that matches their criterias

# all restaurants
restaurant_1 = {
    "name": "North Delish",
    "rating" : 4.5,
    "reservations" : True,
    "services" : ["lunch", "dinner"],
    "price_level" : 3,
    "location": "Rovaniemi"
}

restaurant_2 = {
    "name": "Food Galore",
    "rating" : 2,
    "reservations" : False,
    "services" : ["breakfast", "dinner"],
    "price_level" : 4,
    "location": "London"
}

restaurant_3 = {
    "name": "Snacksy Ltd",
    "rating" : 3.2,
    "reservations" : False,
    "services" : ["breakfast", "lunch"],
    "price_level" : 2,
    "location": "Berlin"
}

restaurant_4 = {
    "name": "Santa's Salmon Place",
    "rating" : 2.7,
    "reservations" : True,
    "services" : ["breakfast", "lunch", "dinner"],
    "price_level" : 1,
    "location": "Rovaniemi"
}

restaurant_5 = {
    "name": "Pure Pizza",
    "rating" : 4.8,
    "reservations" : False,
    "services" : ["lunch", "dinner"],
    "price_level" : 4,
    "location": "Lisbon"
}

restaurant_6 = {
    "name": "Vualya",
    "rating" : 5.0,
    "reservations" : True,
    "services" : ["dinner"],
    "price_level" : 2,
    "location": "Paris"
}

# lists of restaurants
restaurants = [restaurant_1, restaurant_2, restaurant_3, restaurant_4, restaurant_5, restaurant_6]
match_restaurant = []

# questions
rating = int(input("Which star rating at least for the restaurant? (1-5) \n"))
price_level = int(input("What is the maximum price level you're looking for? (1-5) \n"))
reservation = input("Would you like to make a reservation before hand? (y/n)\n")
time = int(input("In what time would you like to arrive? (0 – 23)\n"))

# timing into services
if 6 <= time <= 10:
    time = "breakfast"
elif 11 <= time <= 16:
    time = "lunch"
elif 17 <= time <= 24:
    time = "dinner"
elif 0 <= time <= 5:
    time = "night"

# reservation into variables
if reservation == "y":
    reservation = True
elif reservation == "n":
    reservation = False

# checking conditions
for restaurant in restaurants:
    name = restaurant["name"]
    if rating <= restaurant['rating']:
        if price_level >= restaurant['price_level']:
            if time in restaurant["services"]:
                if reservation == False:
                    match_restaurant.append(name)
                elif reservation == True:
                    continue

# count number of res in the list
number_of_restaurants = len(match_restaurant)

# print results of selection
if number_of_restaurants > 0:
    print(f"You can visit these restaurants:", ', ' .join(match_restaurant))
else:
    print("No matching restaurants found, unfortunately!")
