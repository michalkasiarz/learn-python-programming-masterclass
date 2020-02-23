# Dictionary for loop

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# printing all the values from dictionary
for snack in fruit:
    print(fruit[snack])

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack] + ".")
    print('-' * 10)
