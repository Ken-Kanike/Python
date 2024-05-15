"""
#Funtions
#user def funtion
#function definition
def user_def():
    print("This is a user def function")
#function calling    
user_def()    

#function parameter/ argument passing
def squareDemo(side):
    print("Square of %d = %d " %(side,side*side))
squareDemo(4)
squareDemo(int(input("Enter a number to find square : ")))

#return statement
def cubeDemo(n):
    return n*n*n
print("Cube of 3 = ",cubeDemo(3))


#WAP to swap using function
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a , b   # a , b = b , a
a = 10;
b = 20;
print("Before swapping a = %d , b= %d"%(a,b))
a , b = swap(a,b)
print("After swapping a = %d , b= %d"%(a,b))

#WAP using fucniton to reverse a given number
def reverseNum(n):
    rev = 0
    while(n > 0):
        remainder= n % 10
        rev =rev * 10 + remainder
        n = n//10
    return rev
result = reverseNum(234)
print("Reverse num = ",result)


# #WAP using fucniton to reverse a given string  !!!!!!!!!!!!!!!!
# def reverseStr(str):
#     strArr = list(str)
#     reverseArr = strArr.reverse()
#     reverseStr = reverseArr.
#     return reverseStr
# result = reverseStr("hello")
# print("Reverse num = ",result)


#def to find facorial of a given number
def fact(n):
    if(n == 1 ):
        return n
    else:
        return n*fact(n-1)
num = 5
if(num < 0):
    print("Cant find factorial of Negative number ")
elif(num == 0):
    print("Factorial of 0 is 1")
else:
    print("The factorial of %d is : %d" %(num, fact(num)))

# def for leap year
def leap(year):
    if(year% 4 == 0) and (year% 100 != 0):
        print(year , " is a Leap Year")
    elif(year% 400 == 0):
        print(year , " is a Leap Year")
    # elif(year% 100 == 0):
    #     print(year , " is not a Leap Year")
    else:
        print(year , " is not a Leap Year")
leap(int(input("Enter the year to find leap year : ")))

#WAP tolist of prime numbers in a give range !!!!!!!!!!!!!!!! not sure
def prime(lower,upper):
    primeset = set() # to remove duolicates
    for num in range(lower,upper+1):
        if num > 1:
            for i in range(2,num):
                if num % i ==0:
                    break
                else:
                    primeset.add(num)
    return primeset

print("Enter the range to find the list of prime numbers")
lower = int(input("Start: "))
upper = int(input("End: "))
print("The prime numbers are ..." , prime(lower,upper))

#WAP to find perfect number
def perfect_num(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    if sum == n:
        print(n ," is a perfect number")
    else:
        print(n ," is not a perfect number")
perfect_num(28)

#wap to print all square numbers between 1 to 30
def print_square():
    sqlist = list()
    for i in range(1,30):
        sqlist.append(i**2)
    print(sqlist)
print_square()


#-------------------------------------------------------------------------------
#Modules

#importing
import math
from math import sqrt
from math import sqrt as sq

#get the currrent module name
print("Name of this module is :", __name__)


#creating and importing module
import chapter1
chapter1.intro()
chapter1.generateFibbo(10)

#built in modules
import numbers
import fractions
import itertools
import math

#math module
print(math.sqrt(25))
print(math.gcd(12,15)) # greatest common divisor
print(math.factorial(5))
print(math.pow(2,3))
print(math.remainder(10,3))
print(math.pi)
print(math.ceil(23.24))
print(math.floor(23.24))
#print(math.isfinite())
print(math.exp(2))
print(math.log(10,5))
print(math.cos(90))
print(math.sin(90))
print(math.tan(90))
print(math.e)

#itertools module
num = [1,2,3,4]
print(list(itertools.combinations(num,3)))
print(list(itertools.product(num,repeat=2)))
print(list(itertools.repeat(10,3)))

# map function
names = ['apple','mango','banana','kiwi']
lengths = list(map(len,names))
print(lengths)

#namespace
def print_square(): #global namespace
    sqlist = list() #local namespace
    for i in range(1,30):
        sqlist.append(i**2)
    print(sqlist)
print_square()
print(math.sqrt(24)) #built-in namespace



#-------------------------------------------------------------------------------
#packages


import MyMathPackage.Add.addition as add   #-------- not collable
import MyMathPackage.Sub.subtraction
import MyMathPackage.Mul.multiplication
from MyMathPackage.Div import division as div

print(add(20,10))
print(MyMathPackage.Sub.subtraction(20,10))
print(MyMathPackage.Mul.multiplication(20,10))
print(div(20,10))


# standard packages
# installations
# pip install numpy 
# pip install scipy
# pip install matplotlib
# pip install pandas 

#numpy
import numpy as np
arr= [1,2,3,4,5]
np_arr = np.array(arr)
print(np_arr)

print(np.log(8))
print(np.log2(8))


#scipy
from scipy.special import cbrt
cb = cbrt([27,125])
print(cb)

#matplotlib
import matplotlib.pylab as plt

#WAP to draw a line
arr =[5,10,15,20,25]
a=np.array(arr)
plt.plot(a)
plt.show()

#wap to plot a bar graph
x=[2,4,6]
y=[5,10,8]
plt.bar(x,y)
plt.show()

#wap to plot scattered points
x=[2,4,6,8]
y=[5,10,8,5]
plt.scatter(x,y)
plt.show()

#wap to plot parabola
t = np.linspace(0,1,100)
plt.plot(t,t**2)
plt.show()

#wap to plot 2d graph
# Create a new figure
plt.figure()
# Generate some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# Plot the data
plt.plot(x, y)
# Add a title
plt.title('A Simple 2D Plot')
# Add labels to the x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# Display the grid
plt.grid(True)
# Show the plot
plt.show()

#Pandas
import pandas as pd
import numpy as np

#pandas data stuctures

#series in pandas => 1D e.g list  but immutable
a = np.array(['A','B','C','D','E'])
s = pd.Series(a)
print(s)


#DataFrame => 2D e.g table but mutable
#create table using 2D list
a=[[10,20],[30,40]]
data_fr = pd.DataFrame(a)
print(data_fr)
#create table using dictionary
a={'Empno':[101,102,103],'EmpName':['person1','person2','person3'],'Salary':[10000,15000,25000]}
data_fr = pd.DataFrame(a)
print(data_fr)


#panel => 3D and mutable e.g 3D labelled array
# Create some sample data (2 items, 3 major_axis, 4 minor_axis)
data = np.random.randn(2, 3, 4)
# Create a panel
panel = pd.Panel(data)
# Convert the panel to a DataFrame
df = panel.to_frame()
print(df)

"""












































'''
inistallations-----------------------------------------------------------------------------------------------
PS /path/to/project> pip install numpy 
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: numpy in /path/to/python\site-packages (1.26.4)
PS /path/to/project> pip install scipy
Defaulting to user installation because normal site-packages is not writeable
Collecting scipy
  Downloading scipy-1.13.0-cp312-cp312-win_amd64.whl.metadata (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.6/60.6 kB 402.7 kB/s eta 0:00:00
Requirement already satisfied: numpy<2.3,>=1.22.4 in /path/to/python\site-packages (from scipy) (1.26.4)
Downloading scipy-1.13.0-cp312-cp312-win_amd64.whl (45.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.9/45.9 MB 163.1 kB/s eta 0:00:00
Installing collected packages: scipy
Successfully installed scipy-1.13.0
PS /path/to/project> pip install matplotlib
Defaulting to user installation because normal site-packages is not writeable
Collecting matplotlib
  Downloading matplotlib-3.8.4-cp312-cp312-win_amd64.whl.metadata (5.9 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.2.1-cp312-cp312-win_amd64.whl.metadata (5.8 kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Downloading fonttools-4.51.0-cp312-cp312-win_amd64.whl.metadata (162 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 162.8/162.8 kB 82.0 kB/s eta 0:00:00
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl.metadata (6.5 kB)
Requirement already satisfied: numpy>=1.21 in /path/to/python\site-packages (from matplotlib) (1.26.4)
Collecting packaging>=20.0 (from matplotlib)
  Downloading packaging-24.0-py3-none-any.whl.metadata (3.2 kB)
Collecting pillow>=8 (from matplotlib)
  Downloading pillow-10.3.0-cp312-cp312-win_amd64.whl.metadata (9.4 kB)
Collecting pyparsing>=2.3.1 (from matplotlib)
  Downloading pyparsing-3.1.2-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: python-dateutil>=2.7 in /path/to/python\site-packages (from matplotlib) (2.9.0.post0)  
Requirement already satisfied: six>=1.5 in /path/to/python\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
Downloading matplotlib-3.8.4-cp312-cp312-win_amd64.whl (7.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.7/7.7 MB 125.6 kB/s eta 0:00:00
Downloading contourpy-1.2.1-cp312-cp312-win_amd64.whl (189 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 189.9/189.9 kB 105.5 kB/s eta 0:00:00
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.51.0-cp312-cp312-win_amd64.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 128.3 kB/s eta 0:00:00
Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl (56 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.0/56.0 kB 419.9 kB/s eta 0:00:00
Downloading packaging-24.0-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.5/53.5 kB 138.6 kB/s eta 0:00:00
Downloading pillow-10.3.0-cp312-cp312-win_amd64.whl (2.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 110.6 kB/s eta 0:00:00
Downloading pyparsing-3.1.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.2/103.2 kB 186.0 kB/s eta 0:00:00
Installing collected packages: pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, matplotlib
  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in '/home/user\AppData\Roaming\Python\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed contourpy-1.2.1 cycler-0.12.1 fonttools-4.51.0 kiwisolver-1.4.5 matplotlib-3.8.4 packaging-24.0 pillow-10.3.0 pyparsing-3.1.2  
PS /path/to/project> pip install pandas    
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pandas in /path/to/python\site-packages (2.2.2)
Requirement already satisfied: numpy>=1.26.0 in /path/to/python\site-packages (from pandas) (1.26.4)
Requirement already satisfied: python-dateutil>=2.8.2 in /path/to/python\site-packages (from pandas) (2.9.0.post0)    
Requirement already satisfied: pytz>=2020.1 in /path/to/python\site-packages (from pandas) (2024.1)
Requirement already satisfied: tzdata>=2022.7 in /path/to/python\site-packages (from pandas) (2024.1)
Requirement already satisfied: six>=1.5 in /path/to/python\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
PS /path/to/project> 
'''