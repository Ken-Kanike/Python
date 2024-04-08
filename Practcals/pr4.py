# 1. Write a program to check whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# 2. Write a program to find out absolute value of an input number
number = float(input("Enter a number: "))
absolute_value = abs(number)
print("Absolute value:", absolute_value)


# 3. Write a program to check the largest number among the three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)
print("Largest number:", largest)


# 4. Write a program to check if the input year is a leap year of not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# 5. Write a program to check if a Number is Positive, Negative or Zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# 6. Write a program that takes the marks of 5 subjects and displays the grade.
marks = []

for i in range(5):
    subject_mark = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(subject_mark)

average = sum(marks) / 5

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")

