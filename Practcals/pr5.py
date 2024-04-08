# 1. Print the following patterns using loop:
# a.   *
#      **
#      ***
#      ****
for i in range(1, 5):
    print('*' * i)



# b.   * 
#      ***
#      *****
#      ***
#      * 
n = 3  # Number of rows for each part of the pattern
# Upper part of the pattern
for i in range(1, n + 1):
    print("*" * (2*i - 1))
# Lower part of the pattern
for i in range(n - 1, 0, -1):
    print("*" * (2*i - 1))



# c.  1010101
#     10101
#     101 
#     1 
rows = 4
for i in range(rows, 0, -1):
    for j in range(1, i*2):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()



# 2. Write a Python program to print all even numbers between 1 to 100 using while loop.
num = 2
while num <= 100:
    print(num)
    num += 2



# 3. Write a Python program to find the sum of first 10 natural numbers using for loop.
sum = 0
i = 1
while(i<11):
    sum += i 
    i += 1
print("Sum of first 10 natural numbers:", sum)



# 4. Write a Python program to print Fibonacci series.   0, 1, 1, 2, 3, 5, 8......
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 1



# 5. Write a Python program to calculate factorial of a number 4! = 4 × 3 × 2 × 1
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)


# 6. Write a Python Program to Reverse a Given Number
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

print("Reversed number:", reversed_num)



# 7. Write a Python program takes in a number and finds the sum of digits in a number.
num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num = num // 10

print("Sum of digits:", sum_of_digits)



# 8. Write a Python program that takes a number and checks whether it is a palindrome or not.
num = int(input("Enter a number: "))
copy = num
reverse = 0

while num != 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

if reverse == copy:
    print(copy, "is a palindrome")
else:
    print(copy, "is not a palindrome")

