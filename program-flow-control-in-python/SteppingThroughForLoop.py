# Stepping through a For Loop

number = '63,123;321:642 941 332;120'
separators = ''

# extracting separator with a For Loop
for character in number:    # for each character in a number
    if not character.isnumeric():   # if is not numeric
        separators = separators + character     # add the character to the separators


print(separators)