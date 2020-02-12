# If challenge - my solution

# write a small program to ask for a name and an age
# when both values have been entered, check if the person is the right age to go on an 18-30 holiday
# (they must be over 18 and under 31)
# if they are, welcome them to the holiday, otherwise print a polite message refusing them entry
# our programs expect valid input

name = input('Enter your name, please: ')
age = int(input('Enter your age, please: '))

if 18 <= age < 31:
    print('Welcome on holidays, {}!'.format(name))
else:
    print('Sorry, {}! You are of {} does not allow you any holidays.'.format(name, age))


