# Tim's summary challenge solution

print('Please choose: '
      '\n1 - Learn Python'
      '\n2 - Learn Java'
      '\n3 - Go to sleep'
      '\n4 - Go home!'
      '\n5 - Exit')

while True:
    choice = input()

    if choice == '0':
        break
    elif choice in '12345':
        print('You chose {}'.format(choice))