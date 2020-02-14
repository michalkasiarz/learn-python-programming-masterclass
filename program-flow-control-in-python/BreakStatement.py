# Break statement

shopping_list = ['milk', 'eggs', 'vodka', 'bread', 'cucumber', 'spam', 'mushrooms', 'pizza']

# yet another way to exclude 'spam'
for item in shopping_list:
    if item == 'spam':
        break    # break finishes executing the block at a given moment

    print('Buy ' + item)
