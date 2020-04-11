# Writing text file, another example

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

with open("imelda3.txt", "w") as imelda_file:
    print(imelda, file=imelda_file)
