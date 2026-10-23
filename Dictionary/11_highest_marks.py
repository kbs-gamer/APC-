# 11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

student_marks = {
    "Rohit": 88,
    "Sanya": 96,
    "Arjun": 74,
    "Neha": 92,
    "Kunal": 85
}

highest_student = max(student_marks, key=student_marks.get)
highest_marks = student_marks[highest_student]

print("Student Marks:", student_marks)
print(f"Highest Scorer: {highest_student} with {highest_marks} marks.")
