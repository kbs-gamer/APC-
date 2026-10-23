# 13. Create a dictionary containing student names and marks. Calculate the average marks of all students.

student_marks = {
    "Rohit": 88,
    "Sanya": 96,
    "Arjun": 74,
    "Neha": 92,
    "Kunal": 85
}

total_marks = sum(student_marks.values())
num_students = len(student_marks)
avg_marks = total_marks / num_students

print("Student Marks:", student_marks)
print(f"Total Marks: {total_marks}")
print(f"Number of Students: {num_students}")
print(f"Average Marks: {avg_marks:.2f}")
