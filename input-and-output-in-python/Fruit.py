import shelve

# Shelve module

fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow, citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, green citrus fruit"

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break

    if dict_key in fruit:
        description = fruit[dict_key]
        print(description)
    else:
        print("We don't have a " + dict_key)

fruit.close()
