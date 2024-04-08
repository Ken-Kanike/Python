# 1. Write a program to convert U.S. dollars to Indian rupees.
us_dollars = float(input("Enter amount in U.S. dollars: "))
conversion_rate = 74.5  # Example conversion rate, you can adjust this accordingly
indian_rupees = us_dollars * conversion_rate
print("Amount in Indian rupees:", indian_rupees)


# 2. Write a program to convert bits to Megabytes, Gigabytes and Terabytes
bits = int(input("Enter bits: "))
megabytes = bits / (8 * 1024 * 1024)
gigabytes = bits / (8 * 1024 * 1024 * 1024)
terabytes = bits / (8 * 1024 * 1024 * 1024 * 1024)
print("Equivalent in Megabytes:", megabytes)
print("Equivalent in Gigabytes:", gigabytes)
print("Equivalent in Terabytes:", terabytes)


# 3. Write a program to find the square root of a number
import math 
number = float(input("Enter a number: "))
square_root = math.sqrt(number)
print("Square root:", square_root)


# 4. Write a program to find the area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle:", area)


# 5. Write a program to calculate area and perimeter of the square
side = float(input("Enter side length of square: "))
area = side ** 2
perimeter = 4 * side
print("Area of square:", area)
print("Perimeter of square:", perimeter)


# 6. Write a program to calculate surface volume and area of a cylinder.
import math
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
surface_area = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius ** 2 * height
print("Surface area of cylinder:", surface_area)
print("Volume of cylinder:", volume)


# 7. Write a program to swap the value of two variables
a = input("Enter value for variable a: ")
b = input("Enter value for variable b: ")
print("Before swapping - a:", a, "b:", b)
temp = a
a = b
b = temp
print("After swapping - a:", a, "b:", b)

#or 

# a = input("Enter value for variable a: ")
# b = input("Enter value for variable b: ")
# print("Before swapping - a:", a, "b:", b)
# a, b = b, a
# print("After swapping - a:", a, "b:", b)

