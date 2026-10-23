# 1. Create a dictionary containing student details (roll number, name, department, marks).
# Display all key-value pairs.

student = {
    "roll_no": 101,
    "name": "Aarav Sharma",
    "department": "Computer Science",
    "marks": 92.5
}

print("Student Details:")
for key, value in student.items():
    print(f"  {key}: {value}")
