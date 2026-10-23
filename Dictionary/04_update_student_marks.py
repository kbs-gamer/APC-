# 4. Create a dictionary containing student marks. Update the marks of a specified student.

student_marks = {
    "Aarav": 85,
    "Bhavna": 78,
    "Chetan": 92,
    "Divya": 65
}

print("Original Marks:", student_marks)

student_to_update = "Bhavna"
updated_marks = 88
student_marks[student_to_update] = updated_marks

print(f"Updated marks for {student_to_update} to {updated_marks}")
print("Updated Marks Dictionary:", student_marks)
