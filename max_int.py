# We want to find the maximum positive integer input by a user.

# 1. Prompt the user for a positive integer input.
# 2. Prompt the user for repeated inputs until a negative value is entered.
# 3. If the new value is higher than the value before, log as the highest value
# 4. Repeat until a negative value is entered
# 5. Print the maximum positive integer


num_int = int(input("Input a number: "))
max_int = num_int

while num_int > 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)
