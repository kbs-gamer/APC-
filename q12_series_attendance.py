"""Q12. Series: student names -> attendance %"""
import pandas as pd

attn = pd.Series({"Amit": 92, "Riya": 70, "Karan": 60, "Sneha": 95, "Rahul": 78})
print("Series:\n", attn)
print("\nAverage attendance:", attn.mean())
print("\nAttendance below 75%:\n", attn[attn < 75])
print("\nAttendance above 90%:\n", attn[attn > 90])
print("\nHighest attendance:", attn.idxmax(), "->", attn.max())
