# Iterators challenge - my solution

# Create a list of items (strings or numbers), then create an iterator
# using inter() function.
# Use a for loop to loop n times, where n is the number of items
# in your list.
# Each time round the loop, use next() on your list to print next item.
# hint: use the len() function

animals = ["dog", "cat", "hippo", "horse", "parrot"]
# animals are iterable either way...
iterable_animals = iter(animals)

for animal in range(len(animals)):
    print(next(iterable_animals))

