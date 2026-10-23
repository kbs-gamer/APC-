# 5. Create a dictionary of cities and their populations. Remove a specified city from the dictionary.

cities_population = {
    "Mumbai": 12442373,
    "Delhi": 11007835,
    "Bangalore": 8443675,
    "Hyderabad": 6731790,
    "Ahmedabad": 5577940
}

print("Original Cities:", cities_population)

city_to_remove = "Hyderabad"
if city_to_remove in cities_population:
    removed_pop = cities_population.pop(city_to_remove)
    print(f"Removed {city_to_remove} (Population: {removed_pop})")

print("Updated Cities Dictionary:", cities_population)
