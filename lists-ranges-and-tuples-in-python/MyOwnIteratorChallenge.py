# My own iterator challenge
# User can iterate through the range manually

given_range = input("Give the highest number to iterate up to, "
                    "but not including: ")

print("OK, so you are going to iterate up to {}.".format(given_range))
iterable_range = iter(range(int(given_range)))

user_input = ''

while user_input != 'exit':
    if user_input == 'n':
        try:
            print(next(iterable_range))
        except StopIteration:
            print("Woops! That would be all!")
            break
    else:
        print("Press 'n' for next iteration, 'exit' for exit.")

    user_input = input()
