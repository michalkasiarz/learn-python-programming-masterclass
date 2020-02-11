# slicing idioms

letters = "abcdefghijklmnopqrstuvwxyz"

# reversing a sequence
reversed_sequence = letters[::-1]
print(reversed_sequence)

# extracting specific number of last items from a sequence: 4
lastFourItems = letters[-4::]
print(lastFourItems)

# extracting the first item: two ways to do that
firstItem = letters[:1]         # takes all values up to but not including index 1; when empty, takes empty
firstItemAgain = letters[0]    # extracting explicitly a value from index 0
print(firstItem)
print(firstItemAgain)

# empty string here and its first element to extract, does not produces an error
emptyString = ''
firstOfEmptyString = emptyString[:1]
print(firstOfEmptyString)


