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

