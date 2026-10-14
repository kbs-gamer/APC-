"""Q15. patients.csv (keep patients.csv in the same folder as this file)"""
import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60:\n", df[df["Age"] > 60])
print("\nAverage medical expense:", df["Medical_Expense"].mean())
print("\nPatient with highest medical expense:\n", df.loc[df["Medical_Expense"].idxmax()])
print("\nPatients for each disease:\n", df["Disease"].value_counts())
print("\nExpense above 50,000:\n", df[df["Medical_Expense"] > 50000])
