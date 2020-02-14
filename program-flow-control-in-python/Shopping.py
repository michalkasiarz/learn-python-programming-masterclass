shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# one way to exclude 'spam'
for item in shopping_list:
    if item != 'spam':
        print('Buy ' + item)

print()

# another way to exclude 'spam'
for item in shopping_list:
    if item == 'spam':
        continue

    print('Buy ' + item)