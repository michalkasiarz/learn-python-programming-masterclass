# Summary section challenge
'''
Write a program to print a number of options, and allow the user
to select and option from the list.
The options should be numbered from 1 to 9 - although you can use
less than 9 option if you want.
Make sure there are at least 4 options.
The program should continue looping, allowing the user to choose
one of the options each time round.
The loop should only terminate when the user chooses 0.
If the user makes a valid choice, the program should print
a short message.
The message should include the value that they typed.
If their options isn't one of the options in the menu,
nothing should be printed, although you will see their input
on the screen.
Modify the program so that the menu is printed again, if they choose
an invalid option.
'''

while isPlaying:
    user_choice = int(input('\n\nHello! Choose an option here:\n\n'
                            '\t1) Learn Python'
                            '\t2) Learn Java'
                            '\t3) Go to bed'
                            '\t4) Sing a song\n\n'))

    while user_choice != 0:
        if user_choice == 1:
            print('Your choice: {}. Learn Python, man!'.format(user_choice))
            break
        elif user_choice == 2:
            print('Your choice: {}. Learn Java, man!'.format(user_choice))
            break
        elif user_choice == 3:
            print('Your choice: {}. Going to sleep!'.format(user_choice))
            break
        elif user_choice == 4:
            print('Your choice: {}. Hohoho!'.format(user_choice))
            break
        else:
            print('Your choice: {}. This choice is invalid. Choose again, please.'
                  .format(user_choice))
            break
print('Game over.')