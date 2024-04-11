# 1. Write a Python program to create a user defined module that will ask your college name and will display the name of the college.
#Steps:
# 1 :create a  file named `pr12_Q1college_module.py
# 3:Now, you can import this module and use its functions in another Python script:

import pr12_Q1college_module as college

name = college.get_college_name()
college.display_college_name(name)



# 2. Write a Python program that will calculate area and circumference of circle using inbuilt Math Module
import math
r=int(input("Enter the Radius"))
a=math.pi*r**2
c=2*math.pi*r
print("Area Circle=",a)
print("Circumference Circle =",c)


# 3. Write a Python program that will display Calendar of given month using Calendar Module
import calendar
def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]}, {year}:\n")
    print(cal)

# Input the year and month
year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
display_calendar(year, month)

# or ---------
import calendar
def display_calendar2(year, month):
    print("\nCalendar:")
    print(calendar.month(year, month))

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
display_calendar2(year,month)
