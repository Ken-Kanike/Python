#Write a program to find sum of digits of an integer number, input by the user.
# Input from the user
user_input = input("Enter an integer: ")

# Calculate and print the sum of digits if the input is a valid integer
if user_input.isdigit():
    print("Sum of digits:", sum(map(int, user_input)))
else:
    print("Invalid input. Please enter a valid integer.")
