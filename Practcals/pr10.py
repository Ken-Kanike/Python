# 1. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case_letters(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
# Example usage:
string = "Hello World"
upper, lower = count_case_letters(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)


# 2. Write a Python program to generate a random float where the value is between 5 and 50 using Python math module
import random
def generate_random_float():
    return random.uniform(5, 50)

# Example usage:
random_float = generate_random_float()
print("Random float between 5 and 50:", random_float)


