country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country":"France",
        "Visits":12,
        "cities":["paris","Lille","Dijon"]
    },
    {
         "country":"France",
         "Visits":5,
         "cities":["Berlin","Hamburger"]
    }
]

def getNewCities(country,visits,list_cities):
        new_country = {}
        new_country["country"] = country
        new_country["visits"] = visits
        new_country["cities"] = list_cities
        travel_log.append(new_country)

getNewCities(country=country,visits=visits,list_cities=list_of_cities)

print(travel_log)

