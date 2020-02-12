# Checking not in
# string comparisons are case-sensitive!

activity = input('What would you like to do today? ')

if 'cinema' not in activity.casefold():     # validation with lowering letters
    print('But I want to go to the cinema')
else:
    print('You were sayin\' anythin\' about cinema?')
