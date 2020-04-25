# Functions changed


def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text) // 2)
    print(" " * left_margin, text)


def centre_text(*args, sep=" "):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text) // 2)
    return " " * left_margin + text


# call the function
s1 = centre_text("spam and eggs")
print(s1)
s2 = centre_text(12)
print(s2)
s3 = centre_text("spam, spam and eggs")
print(s3)
s4 = centre_text("spam, spam, spam and spam")
print(s4)
s5 = centre_text("spam, spam, spam and spam")
print(s5)

print("=" + str(12 * 3))
print(sorted(["b", "d", "c", "a"]))

