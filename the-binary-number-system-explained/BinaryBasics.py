# Binary basics - introduction to the section

# binary is based on two: 0 and 1

# decimal to binary up to 16
for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

# decimal to hex
for i in range(17):
    print("{0:>2} in hex is {0:>02x}.".format(i))

x = 0x20
y = 0x0a

print(x)
print(y)
print(x * y)
