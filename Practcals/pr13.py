# 1. Write a Python program to create two matrices and perform addition, subtraction, multiplication and division operation on matrix.
import numpy
x=numpy.array([1,2])
y=numpy.array([7,8])
print("Addition of Matrix ",numpy.add(x,y))
print("Subtraction of Matrix ",numpy.subtract(x,y))
print("Multiplication of Matrix ",numpy.multiply(x,y))
print("Division of Matrix ",numpy.divide(x,y))

#or ---

import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Addition
addition_result = np.add(matrix1, matrix2)
print("Matrix Addition:\n", addition_result)

# Subtraction
subtraction_result = np.subtract(matrix1, matrix2)
print("Matrix Subtraction:\n", subtraction_result)

# Multiplication
multiplication_result = np.matmul(matrix1, matrix2)
print("Matrix Multiplication:\n", multiplication_result)

# Division (element-wise)
division_result = np.divide(matrix1, matrix2)
print("Matrix Division:\n", division_result)

# 2. Write a Python program to concatenate two strings.
str1="Hello"
str2="World"
print("String1 :",str1)
print("String2 :",str2)
print("Concatenated Strings ",(str1+str2))


# 3. Write a NumPy program to generate six random integers between 10 and 30
import numpy as np

random_integers = np.random.randint(10, 31, size=6)
print("Random Integers between 10 and 30:", random_integers)


#Note : type and run this in ur terminal to use numpy
#  pip install numpy   