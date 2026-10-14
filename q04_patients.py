"""Q4. Patients: age > 60, average charge, max charge, charges > 50000"""
import pandas as pd

pat = pd.DataFrame({
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Ramesh", "Sita", "Mohan", "Geeta", "Arjun"],
    "Age": [65, 45, 72, 58, 61],
    "Disease": ["Diabetes", "Fever", "Heart", "Asthma", "Heart"],
    "Medical_Charges": [55000, 3000, 90000, 12000, 70000],
})
print("Patients above 60:\n", pat[pat["Age"] > 60])
print("\nAverage medical charge:", pat["Medical_Charges"].mean())
print("Maximum medical charge:", pat["Medical_Charges"].max())
print("\nCharges > 50,000:\n", pat[pat["Medical_Charges"] > 50000])
