answer = 5

print('Please guess a number between 1 and 10: ')
guess = int(input())

if guess < answer:
    print('Too low!')
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print('Sorry, you\'ve not guessed correctly')
elif guess > answer:
    print('Too high!')
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print('Sorry, you\'ve not guessed correctly')
else:
    print('You got it first time!')
