"""Q9. Series: employee names -> salaries"""
import pandas as pd

sal = pd.Series({"Anil": 60000, "Priya": 45000, "Suresh": 75000,
                 "Neha": 52000, "Vikas": 40000})
print("Series:\n", sal)
print("\nHighest salary :", sal.max())
print("Lowest salary  :", sal.min())
print("Average salary :", sal.mean())
print("\nEmployees earning more than 50,000:\n", sal[sal > 50000])
