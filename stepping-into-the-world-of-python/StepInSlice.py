# using a Step in a Slice

#                   1
#         01234567890123
parrot = 'Norwegian Blue'

print(parrot[0:6:2])    # from index 0, up to but not including index 6 with step every two - Nre
print(parrot[0:6:3])    # from index 0, up to but not including index 6 with step every three - Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]     # extracts separators
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
