# For loops extracting values from user input
# prints entered number without any separators

number = input('Please enter a series of numbers, using any separators you like: ')
separators = ''
numberWithNoSeparators = ''

for char in number:
    if not char.isnumeric():
        separators = separators + char
    else:
        numberWithNoSeparators = numberWithNoSeparators + char

print(separators)
print(numberWithNoSeparators)