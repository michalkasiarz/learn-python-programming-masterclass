# Dictionaries and tuples

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())

# tuple of tuples
print(f_tuple)

# converted to regular dictionary
print(dict(f_tuple))
