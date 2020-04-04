# Sets - UNORDERED

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# printing set with even numbers
even = set(range(0, 40, 2))
print(even)

print()

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

print("=============")

# using union
even = set(range(0, 40, 2))
print("Even: " + str(even))
print(str(len(even)) + " elements")

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("Squares: " + str(squares))
print(str(len(squares)) + " elements")

print("=============")

print("even.union(squares): " + str(even.union(squares)))
print(str(len(even.union(squares))) + " elements")
print("squares.union(even): " + str(squares.union(even)))

print("=============")

# using intersection - present the number present in both sets
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("=============")

even = set(range(0, 40, 2))
print("Sorted even: " + str(sorted(even)))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print("Sorted squares: " + str(sorted(squares)))
print("Even minus squares")
print("sorted(even.difference(squares)): " + str(sorted(even.difference(squares))))
print("(sorted(even - squares)): " + str(sorted(even - squares)))
print("squares minus even")
print("str(squares.difference(even))" + str(squares.difference(even)))
print("str(squares - even)" + str(squares - even))

print("=============")

# difference_update method

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("Symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("Symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))
