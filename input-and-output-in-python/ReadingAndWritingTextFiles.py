jabber = open(r"C:\Users\micha\Documents\buchalka-python\learn-python-programming-masterclass\input-and-output-in-python\original.txt", "r")

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()
