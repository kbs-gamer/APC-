"""Q11. Series: patient IDs (index) -> ages"""
import pandas as pd

age = pd.Series({101: 65, 102: 45, 103: 72, 104: 30, 105: 61})
print("Series:\n", age)
print("\nAverage age        :", age.mean())
print("Oldest patient ID  :", age.idxmax(), "(age", age.max(), ")")
print("Youngest patient ID:", age.idxmin(), "(age", age.min(), ")")
print("\nPatients above 60:\n", age[age > 60])
