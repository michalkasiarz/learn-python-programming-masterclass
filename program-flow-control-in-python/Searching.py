# searching for an index of an item

shopping_list = ['milk', 'eggs', 'vodka', 'bread', 'cucumber', 'spam', 'mushrooms', 'pizza']

item_to_find = 'vodka'
found_at = None

# for index in range of the list
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break   # if an item is found, the loop is ended

if found_at is not None:
    print('Item found at position {}.'.format(found_at))
else:
    print('Not found at position {}'.format(item_to_find))

print()

# better way to write this code

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print('Item found at position {}.'.format(found_at))
else:
    print('Not found at position {}'.format(item_to_find))