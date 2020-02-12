# Using and, or, in Conditions

age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time!")
else:
    print("Have a good day at work!")

