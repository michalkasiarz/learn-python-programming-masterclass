# Truthy values
# 3 most built-in objects considered false in Python:
#   1) constants like None and False
#   2) zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#   3) empty sequences and collections: '', (), [], {}, set(), range(0)

name = input('Please enter your name: ')
if name != '':
    print('Hello, {}!'.format(name))
else:
    print('Are you the man with no name?')
