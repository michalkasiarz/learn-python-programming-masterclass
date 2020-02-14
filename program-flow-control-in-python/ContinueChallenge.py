# Continue challenge

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5
# Zero is considered divisible by everything (zero should not appear in the output)
# The aim is to use the continue statement, but it's also possible to do this without continue

# while loop solution - continue not used
num = 0
while num < 21:
    if num % 3 != 0 and num % 5 != 0:
        print(num)
    num += 1

print()

# for loop solution with continue statement
for num in range(1, 21):
    if num % 3 == 0 or num % 5 == 0:
        continue

    print(num)