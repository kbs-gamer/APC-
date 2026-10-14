"""Q13. students.csv (keep students.csv in the same folder as this file)"""
import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("\nTotal and Average of each student:\n", df[["Name", "Total", "Average"]])

print("\nStudents with average > 75:\n", df[df["Average"] > 75])
print("\nStudent with highest average:\n", df.loc[df["Average"].idxmax()])
print("\nAverage marks of each subject:\n", df[["Python", "DBMS", "Maths"]].mean())
