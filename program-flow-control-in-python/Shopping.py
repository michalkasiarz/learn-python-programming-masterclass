shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# one way to exclude 'spam'
for item in shopping_list:
    if item != 'spam':
        print('Buy ' + item)

print()

# another way to exclude 'spam'
for item in shopping_list:
    if item == 'spam':
        continue    # continue causes all the remaining code in the block to be skipped

    print('Buy ' + item)