def reverse_number(num):
    # Initialize a variable to store the reverse of the number
    reverse = 0
    
    # Iterate through each digit of the number
    while num > 0:
        # Extract the last digit of the number
        digit = num % 10
        # Append the digit to the reverse number
        reverse = (reverse * 10) + digit
        # Remove the last digit from the number
        num = num // 10
    
    # Return the reverse of the number
    return reverse

# Take input from the user
number = int(input("Enter a number: "))

# Call the user-defined function to find the reverse of the number
reverse = reverse_number(number)

# Print the reverse of the number
print("Reverse of the number:", reverse)
