# Write a python program that prints the minimum and maximum of 5 numbers enterred by the user without using built in function

# Initialize variables for min and max
min_number = float('inf')  # set to positive infinity initially
max_number = float('-inf')  # set to negative infinity initially

# Input five numbers from the user
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))

    # Update min and max values
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

# Print the results
print(f"The minimum number is: {min_number}")
print(f"The maximum number is: {max_number}")



