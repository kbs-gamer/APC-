# 10. Accept five student names and their marks from the user and store them in a dictionary.

students = {}
sample_data = [("Aarav", 85.0), ("Diya", 92.0), ("Kabir", 78.0), ("Ananya", 89.0), ("Vivaan", 95.0)]

print("Enter details for 5 students (press enter for defaults):")
for i in range(5):
    try:
        name = input(f"Enter name of student {i+1} (default '{sample_data[i][0]}'): ").strip() or sample_data[i][0]
    except EOFError:
        name = sample_data[i][0]

    try:
        marks_input = input(f"Enter marks for {name} (default {sample_data[i][1]}): ").strip()
        marks = float(marks_input) if marks_input else sample_data[i][1]
    except (EOFError, ValueError):
        marks = sample_data[i][1]

    students[name] = marks

print()
print("Stored Students Dictionary:")
for name, marks in students.items():
    print(f"  {name}: {marks}")
