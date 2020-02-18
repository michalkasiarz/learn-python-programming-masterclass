# Demo on assigning variables

# all variables are assigned the value of 12
a = b = c = d = 12
print(c)

a, b, c, d = 11, 12, 13, 14

print(f"a is {a}")
print(f"b is {b}")
print(f"c is {c}")
print(f"d is {d}")

print()

# firstly, a get value of b, which is 12, then, b get value of a, which is 11)
a, b = b, a
print(f"a is {a}")
print(f"b is {b}")
