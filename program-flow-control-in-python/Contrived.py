# Else in a loop

numbers = [1, 45, 31, 16, 60]

for num in numbers:
    if num % 8 == 0:
        # reject the list
        print('The numbers unacceptable')
        break
else:   # only when loop ends normally, without break
    print('All those numbers are fine.')