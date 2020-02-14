# Nested for loops

for i in range(1, 13):
    for j in range(1, 13):
        print('{} times {} is {}.'.format(j, i, i * j))
    print('---------------')