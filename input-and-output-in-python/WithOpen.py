# With open; it closes the file when you are done

with open(r"C:\Users\micha\Documents\buchalka-python\learn-python-programming-masterclass\input-and-output-in-python\original.txt", "r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")
