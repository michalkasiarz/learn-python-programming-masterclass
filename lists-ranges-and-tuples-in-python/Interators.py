# Iterators

string = "1234567890"

for char in string:
    print(char)

print()


my_iterator = iter(string)
print(my_iterator)      # prints memory allocation of the object
print(next(my_iterator))    # prints the first result of the iteration - 1
print(next(my_iterator))    # prints the second result of the iteration - 2
print(next(my_iterator))    # prints the third result of the iteration - 3

