# Write a python program to implement a formula e = mc square . states that the equivalent energy e can be calculated as mass (m) x  the light 's speed . c = about 3x10^8 m/s^2 . WAP to accept the mass of an object and determine its energy

def calculate_energy(mass):
    # Speed of light (c) in meters per second
    speed_of_light = 3 * 10**8

    # Calculate energy using the formula E = mc^2
    energy = mass * speed_of_light**2

    return energy


# Input the mass of the object
mass = float(input("Enter the mass of the object in kilograms: "))

# Calculate energy using the function
energy = calculate_energy(mass)

# Display the result
print(f"The energy of the object is: {energy} joules")


