# 12. Create a dictionary containing student names and marks. Find the student with the lowest marks.

student_marks = {
    "Rohit": 88,
    "Sanya": 96,
    "Arjun": 74,
    "Neha": 92,
    "Kunal": 85
}

lowest_student = min(student_marks, key=student_marks.get)
lowest_marks = student_marks[lowest_student]

print("Student Marks:", student_marks)
print(f"Lowest Scorer: {lowest_student} with {lowest_marks} marks.")
