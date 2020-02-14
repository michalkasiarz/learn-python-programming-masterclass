# searching for an index of an item

shopping_list = ['milk', 'eggs', 'vodka', 'bread', 'cucumber', 'spam', 'mushrooms', 'pizza']

item_to_find = 'vodka'
found_at = None

# for index in range of the list
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index

print('Item found at position {}.'.format(found_at))