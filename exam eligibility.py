# List of eligible students with their names and hall number
eligible_students = [
    {"roll_number": 1, "name": "rohan", "hall_number": 1},
    {"roll_number": 2, "name": "ram", "hall_number": 1},
    {"roll_number": 3, "name": "sam", "hall_number": 1},
    {"roll_number": 4, "name": "venpa", "hall_number": 1},
    {"roll_number": 5, "name": "kumar", "hall_number": 1},
    {"roll_number": 6, "name": "tom", "hall_number": 1},
    {"roll_number": 7, "name": "ranga", "hall_number": 1},
    {"roll_number": 8, "name": "nitish", "hall_number": 1},
    {"roll_number": 1, "name": "harsha", "hall_number": 2},
    {"roll_number": 2, "name": "aadhi", "hall_number": 2},
    {"roll_number": 3, "name": "viswa", "hall_number": 2},
    {"roll_number": 4, "name": "ajay", "hall_number": 2},
    {"roll_number": 5, "name": "emma", "hall_number": 2},
    {"roll_number": 6, "name": "noah", "hall_number": 2},
    {"roll_number": 7, "name": "ellie", "hall_number": 2},
    {"roll_number": 8, "name": "andrew", "hall_number": 2},
]

# Function to check if a student is eligible
def check_eligibility(name):
    for student in eligible_students:
        if student["name"].lower() == name.lower():
            return f"{name.capitalize()} is eligible with Roll Number: {student['roll_number']} and Hall Number: {student['hall_number']}."
    return f"{name.capitalize()} is not eligible."

# Take input from the user
user_name = input("Enter the student's name: ")

# Check and print the eligibility
eligibility = check_eligibility(user_name)
print(eligibility)
