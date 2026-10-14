"""Q6. Attendance %, students below 75%"""
import pandas as pd

att = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Riya", "Karan", "Sneha", "Rahul"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [90, 70, 60, 85, 74],
})
att["Attendance_Percentage"] = (att["Classes_Attended"] / att["Total_Classes"]) * 100
print(att)
print("\nStudents with attendance below 75%:\n", att[att["Attendance_Percentage"] < 75])
