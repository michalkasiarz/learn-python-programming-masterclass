# Augmented assignment in a loop

# Early computers could only perform addition.
# In order to multiply one number by another, the performed repeated addition.
# For example, 5 * 8 was performed by adding 5 eight times:
# 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40
# Use a for loop, and augmented assignment to give answer the result
# of multiplying number by multiplier

number = 5
multiplier = 5
answer = 0

# add your loop after this comment
for num in range(multiplier):
    answer += number

print(answer)
