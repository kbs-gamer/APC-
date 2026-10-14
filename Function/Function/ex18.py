def result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


marks = []

for i in range(5):
    mark = float(input("Enter marks: "))
    marks.append(mark)

percentage, grade = result(marks)

print("Percentage =", percentage)
print("Grade =", grade)