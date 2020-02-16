# Introduction to lists

# ip_address = input("Please enter an IP address: ")
# print(ip_address.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
sorted_numbers = sorted(numbers)   # sorted() is a built-in function

print(f"Numbers: {numbers}")
print(f"Sorted_numbers {sorted_numbers}")

if numbers == sorted_numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")

numbers.sort()  # sort() doesn't return anything
print("Sorting numbers...")

print(f"Numbers: {numbers}")
print(f"Sorted_numbers {sorted_numbers}")

if numbers == sorted_numbers:
    print("The lists are equal")
else:
    print("The lists are not equal")




