"""Q3. Products: Total Amount = Price x Quantity, product with highest total sales"""
import pandas as pd

prod = pd.DataFrame({
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Office"],
    "Price": [50000, 500, 1200, 8000, 6000],
    "Quantity": [3, 40, 15, 10, 5],
})
prod["Total_Amount"] = prod["Price"] * prod["Quantity"]
print(prod)
print("\nProduct with highest total sales:\n", prod.loc[prod["Total_Amount"].idxmax()])
