# Challenge
# Modify the program to use a while loop, to allow the player to keep guessing.
# The program should let the player know whether to guess higher or lower, and should
# print a message when the guess is correct.
# A correct guess will terminate the program
# As an optional extra, allow the player to quit by entering 0 (zero) for the guess

import random

# assigns a random number from 1 to 10 to answer variable
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: remove after answering

print('Please guess a number between 1 and {}: '.format(highest))
guess = int(input())
notCorrectGuess = True

while notCorrectGuess:
    if guess < answer:
        print('Too low!')
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it!")
            break
    elif guess > answer:
        print('Too high!')
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it!")
            break
    else:
        print('You got it first time!')
        break
