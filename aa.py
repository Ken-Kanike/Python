import random

# List of 45 questions (Example: Q1 to Q45)
questions = [f"Q{i}" for i in range(1, 46)]

# Function to get questions for a specific roll number
def get_questions_for_roll(roll_number):
    random.seed(roll_number)  # Set seed for reproducibility
    assigned_questions = random.sample(questions, 5)  # Pick 5 unique questions
    return assigned_questions

# Ask for the roll number

try:
    roll_number = int(input("Enter your roll number (1-140): "))  # User input
    if 1 <= roll_number <= 140:
        assigned_questions = get_questions_for_roll(roll_number)
        print(f"\nRoll No {roll_number}, your assigned questions are:")
        for q in assigned_questions:
            print(f"- {q}")
    else:
        print("Invalid roll number! Please enter a number between 1 and 70.")
except ValueError:  
    
    print("Invalid input! Please enter a valid roll number.")    