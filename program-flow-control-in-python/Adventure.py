available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ''
while chosen_exit not in available_exits:
    chosen_exit = input('Please choose a direction: ')

print('Aren\'t you glad to got out of there?')