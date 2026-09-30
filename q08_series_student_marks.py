"""Q8. Series: student names -> marks"""
import pandas as pd

marks = pd.Series({"Amit": 85, "Riya": 70, "Karan": 60, "Sneha": 92, "Rahul": 78})
print("Series:\n", marks)
print("\nMarks of Riya :", marks["Riya"])
print("Maximum marks :", marks.max())
print("Minimum marks :", marks.min())
print("Average marks :", marks.mean())
print("\nStudents who scored more than 75:\n", marks[marks > 75])
