# Extracting capitals challenge
# Write a program to print out the capital letters in the string

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char.isupper():
        print(char)
