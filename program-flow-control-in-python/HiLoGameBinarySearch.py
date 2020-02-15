# Hi-Lo Game - binary search

low = 1
high = 1000

print('Please think of a number betwen {} and {}.'.format(low, high))
input('Press ENTER to start')

guesses = 1
while True:
    print('\tGuessing in the range of {} to {}.'.format(low, high))
    guess = low + (high - low) // 2  # calculates the midpoint
    high_low = input('My guess is {}. Should I guess higher or lower? '
                     'Enter h or l, or c if my guess was correct'
                     .format(guess)).casefold()
    if high_low == 'h':
        # guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == 'l':
        # guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == 'c':
        print('I got in {} guesses!'.format(guesses))
        break
    else:
        print('Please enter h, l or c')

    guesses += 1
