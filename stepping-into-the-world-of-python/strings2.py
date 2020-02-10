parrot = 'Norwegian Blue'

print(parrot)

print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

# negative indexing

print()
print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# negative indexing with subtraction

print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print()
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

# negative indexing with len() function

print()
print(parrot[3 - len(parrot)])
print(parrot[4 - len(parrot)])
print()
print(parrot[3 - len(parrot)])
print(parrot[6 - len(parrot)])
print(parrot[8 - len(parrot)])

print()
print(parrot[0:6])  # up to but not including - Norweg
print(parrot[0:9])  # up to but not including - Norwegian
print(parrot[:9])   # up to but not including - Norwegian
print(parrot[10:])   # Blue
