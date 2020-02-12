# simple condition task with user input and its validation try-except

while True:
    try:
        x = int(input("Give X number: "))
        y = int(input("Give Y number: "))
        break
    except ValueError:
        print("Invalid input. Please type a number.")


if x > y:
    print('X is greater than Y')
elif x < y:
    print('X is smaller than Y')
else:
    print('X equals Y')
