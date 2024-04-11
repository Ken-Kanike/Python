# 1. Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(num):
    for x in range(2,num):
     if num%x ==0 :
        return False
    return True
print("Parameter is Prime",prime(2))


# 2. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(num):
    if num ==0 :
        return 1
    else :
        return num*fact(num-1)
num=int(input("Enter the number :"))
print(fact(num))



# 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
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