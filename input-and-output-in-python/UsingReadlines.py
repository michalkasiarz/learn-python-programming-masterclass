with open(
        r"C:\Users\micha\Documents\buchalka-python\learn-python-programming-masterclass\input-and-output-in-python\original.txt",
        "r") as jabber:
    # converting text to a list
    # readlines() reads the entire file at once
    lines = jabber.readlines()
    print(lines)

for line in lines:
    print(line, end="")

# printing lines through reverse slice
for line in lines[::-1]:
    print(line, end="")

with open(
        r"C:\Users\micha\Documents\buchalka-python\learn-python-programming-masterclass\input-and-output-in-python\original.txt",
        "r") as jabber:
    lines = jabber.read()
    print(lines)

# printing lines through reverse slice and backwards
for line in lines[::-1]:
    print(line, end="")
