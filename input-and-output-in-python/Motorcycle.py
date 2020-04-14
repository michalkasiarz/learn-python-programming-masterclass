import shelve

# Motorcycle example

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["color"])

# for loop print the keys
    for key in bike:
        print(key)
