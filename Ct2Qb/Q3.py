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

# Example usage:
if __name__ == "__main__":
    # Creating an object of Employee
    emp = Employee("", "", 0.0)
    # Reading employee information
    emp.read_employee_info()
    # Printing employee information
    print("\nEmployee Information:")
    emp.print_employee_info()
