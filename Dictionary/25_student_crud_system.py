# 25. Create a dictionary containing student names and marks.
# Develop a program to:
# 1. Add a student
# 2. Update marks
# 3. Delete a student
# 4. Search for a student
# 5. Display all students
# 6. Find the highest marks
# 7. Calculate the average

students = {
    "Aarav": 85,
    "Bhavna": 92,
    "Chetan": 78
}

def add_student(name, marks):
    students[name] = marks
    print(f"Student '{name}' added with {marks} marks.")

def update_marks(name, marks):
    if name in students:
        students[name] = marks
        print(f"Marks updated for '{name}' to {marks}.")
    else:
        print(f"Student '{name}' not found.")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"Student '{name}' deleted.")
    else:
        print(f"Student '{name}' not found.")

def search_student(name):
    if name in students:
        print(f"Found: {name} scored {students[name]} marks.")
    else:
        print(f"Student '{name}' not found.")

def display_all():
    print("\n--- All Students ---")
    for name, marks in students.items():
        print(f"  {name}: {marks}")

def highest_marks():
    top_student = max(students, key=students.get)
    print(f"Highest Scorer: {top_student} ({students[top_student]} marks)")

def average_marks():
    avg = sum(students.values()) / len(students)
    print(f"Class Average: {avg:.2f}")

print("Initial Database:", students)
add_student("Divya", 95)
update_marks("Chetan", 82)
search_student("Aarav")
highest_marks()
average_marks()
delete_student("Bhavna")
display_all()
