# List constructor

list_1 = []
list_2 = list()

print(f"List 1 : {list_1}")
print(f"List 2 : {list_2}")

if list_1 == list_2:    # checking of the equality of lists CONTENT
    print("Lists are equal")

print(list("The lists are equal"))  # list created

even = [2, 4, 6, 8]
another_even = even     # they refer to exact same list here

print(f"Another_even is even? {another_even is even}")

another_even.sort(reverse=True)     # reverse sorting
print(even)

another_even = list(even)   # creating a new list with a constructor

print(f"Another_even is even? {another_even is even}")

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
numbers = [even, odd]   # returns a new list containing two lists
print(numbers)

for number_set in numbers:
    print(number_set)       # prints a whole list

    for value in number_set:
        print(value)        # print values of a list, one by one
