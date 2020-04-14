import shelve

# Shelve module

fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow, citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, green citrus fruit"

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break

    description = fruit.get(shelf_key, "We don't have a " + shelf_key)
    print(description)

fruit.close()
