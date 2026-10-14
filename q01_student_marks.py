"""Q1. Student marks: DataFrame, total, average, students with average > 75"""
import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Riya", "Karan", "Sneha", "Rahul"],
    "Python": [85, 70, 60, 92, 78],
    "DBMS": [80, 65, 55, 88, 72],
    "Maths": [90, 75, 58, 95, 70],
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("\nTotal and Average:\n", df)

print("\nStudents with average > 75:\n", df[df["Average"] > 75])
