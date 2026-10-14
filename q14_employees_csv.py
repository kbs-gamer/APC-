"""Q14. employees.csv (keep employees.csv in the same folder as this file)"""
import pandas as pd

df = pd.read_csv("employees.csv")

print("CSE employees:\n", df[df["Department"] == "CSE"])
print("\nAverage salary :", df["Salary"].mean())
print("Highest salary :", df["Salary"].max())
print("Lowest salary  :", df["Salary"].min())
print("\nSalary > 50,000:\n", df[df["Salary"] > 50000])
print("\nDepartment-wise average salary:\n", df.groupby("Department")["Salary"].mean())
