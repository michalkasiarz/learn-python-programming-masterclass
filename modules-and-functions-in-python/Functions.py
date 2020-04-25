# Functions


def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


def centre_text(*args, sep=" ", end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    print(" " * left_margin, text, end=end, file=file, flush=flush)


with open("centred", mode="w") as centred_file:
    # call the function
    centre_text("spam and eggs", file=centred_file)
    centre_text(12, file=centred_file)
    centre_text("spam, spam and eggs", file=centred_file)
    centre_text("spam, spam, spam and spam", file=centred_file)
    centre_text("spam, spam, spam and spam", 11, 123123, "go", "hello", file=centred_file)


# printing text
a = "Hello"
b = "man"
c = "how"
d = "are"
e = "you"

print(a, b, c, d, e, sep="\n")
