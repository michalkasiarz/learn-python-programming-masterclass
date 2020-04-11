# Reading the content of a text file,
# saving it into a list, and printing the content of the list in the end

cities = []  # empty list
with open("cities.txt", "r") as city_file:  # opening cities with a read mode
    for city in city_file:  # for every city in the text file
        cities.append(city.strip("\n"))  # append a city to a list that has been read from a text file

    print(cities)  # printing cities

    for city in cities:  # for every city in a list of cities
        print(city)  # print city
