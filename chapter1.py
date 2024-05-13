#WAP to find square root
# num = int(input("Enter a number : "))
# square = num**0.5
# print("The Square root of ", num ," is ", square);

#WAP to calculate Simple Interest
# p = int(input("Enter principle amount : "))
# r = float(input("Enter rate of interest : "))
# n = float(input("Enter number of years : "))
# SI = (p*r*n)/100
# print("Simple Interest = ",SI)

#area , permimeter of circle 
# from math import pi as PI
# radius = 10
# area = PI * radius**2  # pi r square 
# perimetre = 2 * PI * radius # 2 pi  r 
# print("Area of Circle = ", area)
# print("Perimeter of circle = ", perimetre)

# celcius -> ferhenite
# f = 95.5
# c = ( f - 32)/ 1.8 
# ferhenite ->  celcius
# f =  (c* 1.8 ) + 32
# print("f = ", f)
# print("C = ", c)


#---- for chapter 4
def intro():
    print("This is chapter 1 file...")

def generateFibbo(n):
    a , b = 0,1
    while b < n:
        print( b, end=" ")
        a,b = b , a+b
    print()