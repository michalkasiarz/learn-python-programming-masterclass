name = input("Please enter your name: ")
age = int(input("How old are you, {0}".format(name)))
print(age)

# checking the condition
if age >= 18:
    print("You are old enough to vote.")
    print("Please put an X in the box.")
else:
    print("You are not old enough to vote. Please come back in {0} years.".format(18 - age))

# checking the condition the other way
if age < 18:
    print("You are not old enough to vote. Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in return in Return of the Jedi.")
else:
    print("You are old enough to vote.")
    print("Please put an X in the box.")
