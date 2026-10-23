# 30. Take a dictionary containing student names and their departments;
# create a new dictionary that groups students according to their department.

student_departments = {
    "Aarav": "CSE",
    "Bhavna": "ECE",
    "Chetan": "CSE",
    "Divya": "MECH",
    "Eshwar": "ECE",
    "Farhan": "CSE",
    "Gauri": "CIVIL"
}

grouped = {}
for student, dept in student_departments.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(student)

print("Original Student-Department Mapping:")
for student, dept in student_departments.items():
    print(f"  {student} -> {dept}")

print("\nGrouped by Department:")
for dept, students in grouped.items():
    print(f"  {dept}: {students}")
