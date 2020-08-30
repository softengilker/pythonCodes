
def validateData( data ):
    return data["ali"]["age"] > list({key: value for (key, value) in people.items() if value["city"] == "samsun"}.values())[0]["age"] and \
           data["can"]["age"] < list({key: value for (key, value) in people.items() if value["city"] == "kars"}.values())[0]["age"]



people = {
    "ali": {
        "city": "a",
        "age": 10
    },
    "berk": {
        "city": "a",
        "age": 10
    },
    "can": {
        "city": "a",
        "age": 10
    },
    "doruk": {
        "city": "a",
        "age": 10
    }
}

cities = ("edirne", "izmir", "kars", "samsun")
ages = (7, 8, 9, 10)
names = ("ali", "berk", "can", "doruk")

for ageIndex in range(4):
    for cityIndex in range(4):
        people["ali"]["age"] = ages[ageIndex]
        people["ali"]["city"] = cities[cityIndex]
        people["berk"]["age"] = ages[ageIndex + 1 if ageIndex + 1 < 4 else (ageIndex + 1) - 4]
        people["berk"]["city"] = cities[cityIndex + 1 if cityIndex + 1 < 4 else (cityIndex + 1) - 4]
        people["can"]["age"] = ages[ageIndex + 2 if ageIndex + 2 < 4 else (ageIndex + 2) - 4]
        people["can"]["city"] = cities[cityIndex + 2 if cityIndex + 2 < 4 else (cityIndex + 2) - 4]
        people["doruk"]["age"] = ages[ageIndex + 3 if ageIndex + 3 < 4 else (ageIndex + 3) - 4]
        people["doruk"]["city"] = cities[cityIndex + 3 if cityIndex + 3 < 4 else (cityIndex + 3) - 4]

        print(people)

        #if validateData(people):
        #    print(people)

print("completed")





