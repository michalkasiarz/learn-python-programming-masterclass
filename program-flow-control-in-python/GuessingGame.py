answer = 5

print('Please guess a number between 1 and 10: ')
guess = int(input())

if guess < answer:
    print('Too low!')
elif guess > answer:
    print('Too high!')
else:
    print('You got it first time!')
