# Presume that a ladder is put upright against a wall. let variables length and angle store , the length of the ladder & the angle that it formes with the ground as it leans against the wall . Write a python program to complete the height reached by the ladder ont the wall for the  following values of length and  angle

# To calculate the height reached by the ladder on the wall, you can use the formula:
# Height = Length × sin(Angle)

import math

def calculate_ladder_height(length, angle):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle)

    # Calculate height using the formula
    height = length * math.sin(angle_radians)

    return height

# Input length and angle from the user
length = float(input("Enter the length of the ladder in feet: "))
angle = float(input("Enter the angle formed with the ground in degrees: "))

# Calculate and display the height reached on the wall
height = calculate_ladder_height(length, angle)
print(f"The height reached by the ladder on the wall is: {height:.2f} feet")

#a) 16 ft , 75 degree  => The height reached by the ladder on the wall is: 15.45 feet
#b) 20 ft , 0 degree => The height reached by the ladder on the wall is: 0.00 feet
#c) 24 ft , 45 degree => The height reached by the ladder on the wall is: 16.97 feet
#d) 24 ft , 80 degree => The height reached by the ladder on the wall is: 23.64 feet
