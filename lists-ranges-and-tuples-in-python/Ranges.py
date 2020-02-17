# Ranges

my_list = list(range(10))
print(my_list)

# ranges converted to lists
even = list(range(0, 100, 2))
odd = list(range(1, 100, 2))

print(even)
print(odd)

# str indexing
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index("e"))
print(my_string[4])

# range indexing
small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals.index(3))

odd2 = range(1, 100, 2)
print(odd2)

# range indexing
print(odd2[34])

sevens = range(7, 1000000, 7)
x = int(input("Please enter a number less than a million: "))

# checking if a given number is divisible by 7
if x in sevens:
    print("{} is divisible by seven.".format(x))

print(small_decimals)
my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('-' * 40)

for i in range(3, 40, 3):
    print(i)
