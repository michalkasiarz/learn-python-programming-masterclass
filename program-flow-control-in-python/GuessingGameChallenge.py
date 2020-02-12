# Guessing Game challenge - my solution

# Change the condition
# if guess != answer:
# to
# if guess == answer:
# then change the program to give correct results

answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You've got it the first time!")
elif guess < answer:
    print("Too low!")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you've not guessed correctly!")
else:   # guess must be greater than answer
    print("Too high!")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you've not guessed correctly!")

