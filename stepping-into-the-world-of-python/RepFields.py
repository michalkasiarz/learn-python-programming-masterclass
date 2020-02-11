# String replacement fields

age = 24

# coerced to str
print("My age is " + str(age) + " years.")

# using .format
print("My age is {} years".format(age))

# 8 replacement fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}."
      .format(31, "Jan", "March", "May", "July", "August", "Oct", "December"))

# three replacement fields with unordered indexes
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print()

# triple quotes
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
