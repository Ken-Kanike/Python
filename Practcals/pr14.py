# 1. Write a Python program to create a class to print an integer and a character with two methods having the same name but different sequence of the integer and the character parameters. For example, if the parameters of the first method are of the form (int n, char c), then that of the second method will be of the form (char c, int n)
class PrintClass:
    def print_int_char(self, n, c):
        print("Integer:", n)
        print("Character:", c)
    
    def print_char_int(self, c, n):
        print("Character:", c)
        print("Integer:", n)

# Test the class
obj = PrintClass()
obj.print_int_char(5, 'A')
obj.print_char_int('B', 10)

#Note class method names cannot be same , because python does not support method overloading


# 2. Write a Python program to create a class to print the area of a square and a rectangle. The class has two methods with the same name but different number of parameters. The method for printing area of rectangle has two parameters which are length and breadth respectively while the other method for printing area of square has one parameter which is side of square. 
class Area:
    def print_rectangle_area(self, length, breadth):
        print("Area of Rectangle:", length * breadth)

    def print_square_area(self, side):
        print("Area of Square:", side ** 2)

# Test the class
obj = Area()
obj.print_square_area(5)  # Square with side length 5
obj.print_rectangle_area(4,6)  # Rectangle with length 4 and breadth 6

#Note class method names cannot be same , because python does not support method overloading


# 3. Write a Python program to create a class 'Degree' having a method 'getDegree' that prints "I got a degree". It has two subclasses namely 'Undergraduate' and 'Postgraduate' each having a method with the same name that prints "I am an Undergraduate" and "I am a Postgraduate" respectively. Call the method by creating an object of each of the three classes.
class Degree:
    def getDegree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")

# Call the method by creating objects of each class
degree_obj = Degree()
degree_obj.getDegree()

undergraduate_obj = Undergraduate()
undergraduate_obj.getDegree()

postgraduate_obj = Postgraduate()
postgraduate_obj.getDegree()

