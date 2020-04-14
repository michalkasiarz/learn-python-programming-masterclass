import shelve

# Shelve module

fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow, citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])

fruit.close()

print(fruit)
