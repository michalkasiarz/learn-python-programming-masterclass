# Introduction to dictionaries

fruit = {"oragne": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# accessing an element in a dict with a key
print(fruit["lemon"])

# adding an entry to the dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])

# overriding existing value
fruit["pear"] = "something you would like"
print(fruit["pear"])

# deleting an element with del
del fruit["lemon"]
print(fruit)
