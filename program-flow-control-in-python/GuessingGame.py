import random

# assigns a random number from 1 to 10 to answer variable
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: remove after answering

print('Please guess a number between 1 and {}: '.format(highest))
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
