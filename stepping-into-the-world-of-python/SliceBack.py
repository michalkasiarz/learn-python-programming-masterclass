# slicing back here!

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]   # reverses a sequence
print(backwards)

# mini-challenge - my solutions
# first task - create a slice that produces the characters qpo
qpo = letters[-10:-13:-1]   # starts with negative indexing - backwards
print(qpo)

# second task - slice the string to produce edcba
edcba = letters[4::-1]  # starts with positive indexing - forward but reversed
print(edcba)

# third task - slice the string to produce the last 8 characters, in reverse order
# starts with default, i.e. the beginning of the reversed string (z),
# up to but not including the negative index -9 (r)
last8 = letters[:-9:-1]
print(last8)
