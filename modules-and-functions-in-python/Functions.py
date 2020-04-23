# Functions


def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


def centre_text(text):
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text("spam, spam, spam and spam")

# printing text
a = "Hello"
b = "man"
c = "how"
d = "are"
e = "you"

print(a, b, c, d, e, sep="\n")
