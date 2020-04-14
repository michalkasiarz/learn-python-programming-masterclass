import shelve

# Shelve module

fruit = shelve.open("ShelfTest")

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])

fruit.close()
