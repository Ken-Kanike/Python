# 1. Write a Python program to Check for ZeroDivisionError Exception.
try:
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    result = dividend / divisor
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")


# 2. Write a Python program to create user defined exception that will check whether the password is correct or not
class IncorrectPasswordError(Exception):
    pass

def check_password(password):
    correct_password = "password123"
    if password != correct_password:
        raise IncorrectPasswordError("Incorrect password!")

# Test the function
try:
    user_password = input("Enter password: ")
    check_password(user_password)
    print("Password is correct.")
except IncorrectPasswordError as e:
    print("Error:", e)
