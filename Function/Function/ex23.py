def student_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    return total, percentage, grade


name = input("Enter student name: ")
roll = input("Enter roll number: ")

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

total, percentage, grade = student_result(marks)

print("\nStudent Name:", name)
print("Roll Number:", roll)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)