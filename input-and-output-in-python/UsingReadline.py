with open(r"C:\Users\micha\Documents\buchalka-python\learn-python-programming-masterclass\input-and-output-in-python\original.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()
