# TASK: create a dict
# print info from the dict

cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    }
}

# print data from the dictionary
print(cafe['name'])
print(cafe["location"]['address'])
print(cafe["location"]['zip_code'], cafe["location"]["city"])

print()
print(cafe['website'])

# print all services in one line
print(f"Services:" , ', '.join(cafe["categories"]))

