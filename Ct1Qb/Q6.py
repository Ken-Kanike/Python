# Write a python program that takes name and age of the user as import and display a message whather th user is eligible to apply for driving licence or not. ( the eligible age is 18 years and below 80 years)
def check_eligibility(name, age):
    if 18 <= age <= 80:
        print(f"Congratulations, {name}! You are eligible to apply for a driving license.")
    else:
        print(f"Sorry, {name}. You are not eligible to apply for a driving license.")

# Taking user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Checking eligibility
check_eligibility(name, age)


