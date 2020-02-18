# More about ranges

decimals = range(0, 100)
my_range = decimals[3:40:3]

# checking if two ranges are equal
print(my_range == range(3, 40, 3))

print(range(0, 5, 2) == range(0, 6, 2))     # True

print(list(range(0, 5, 2)))     # 0, 2, 4
print(list(range(0, 6, 2)))     # 0, 2, 4

r = range(0, 100)
print(r)

# looping backwards
for i in r[::-5]:
    print(i)

# True
print(range(0, 100)[::-2] == range(99, 0, -2))

backsString = "!egaugnal lufrewop yrev a si nohtyP"

# printing a string backwards
print(backsString[::-1])

r = range(0, 10)

# printing a range backwards with a loop
for i in r[::-1]:
    print(i)

# little challenge

o = range(0, 100, 4)
print(o)
for i in o:
    print(i)
p = o[::5]
print(p)
for i in p:
    print(i)

