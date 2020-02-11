# string formatting

# prints squared and cubed values of a number within a range 1-13
for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

# formatting number printing into columns to the right
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# formatting number printing into columns to the left
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

# formatting number printing into columns to the left and the last centered
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^5}".format(i, i ** 2, i ** 3))

print()

# PI number in different formats
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
