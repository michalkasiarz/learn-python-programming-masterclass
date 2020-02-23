# Dictionary ordered keys task

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# stores keys of fruit in a list
ordered_key = list(fruit.keys())

# sorts the list
ordered_key.sort()

# prints a key: i, and the the value: fruit[i]
for i in ordered_key:
    print(i + " - " + fruit[i])


# the same result here! sorted() function RETURNS a sorted list
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# printing values of dict
for value in fruit.values():
    print(value)
