# 1. Create a class Employee with data members: name, department and salary. Create suitable methods for reading and printing employee information
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
    
    def read_employee_info(self):
        self.name = input("Enter employee name: ")
        self.department = input("Enter employee department: ")
        self.salary = float(input("Enter employee salary: "))
    
    def print_employee_info(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Test the class
emp = Employee("John Doe", "HR", 50000)
emp.print_employee_info()

#or
class Employee2:
    name = ""
    department = ""
    salary = 0
    
    def read_employee_info(self):
        self.name = input("Enter employee name: ")
        self.department = input("Enter employee department: ")
        self.salary = float(input("Enter employee salary: "))
    
    def print_employee_info(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

# Test the class
emp = Employee2()
emp.read_employee_info()
emp.print_employee_info()



# 2. Python program to read and print students information using two classes using simple inheritance.
class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.clg = input("Enter your college name: ")
        self.roll = int(input("Enter your roll number: "))

class Test(Student):
    def display(self):
        print("Name is", self.name)
        print("College name is", self.clg)
        print("Roll number is", self.roll)

obj = Test()  
obj.display()  


# 3. Write a Python program to implement multiple inheritance
class Class1:
    def method1(self):
        print("Method 1 from Class1")

class Class2:
    def method2(self):
        print("Method 2 from Class2")

class MultiDerived(Class1, Class2):
    def method3(self):
        print("Method 3 from MultiDerived")

obj = MultiDerived()

obj.method1()  
obj.method2()  
obj.method3()


