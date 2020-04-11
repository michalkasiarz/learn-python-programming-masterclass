# Writing text files

cities = ["Adeladie", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", "w") as city_file:
    for city in cities:
        # passing an argument to file=
        print(city, file=city_file)

