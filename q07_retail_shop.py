"""Q7. Retail shop: Total_Sales column, sales > 10000, max sales, average sales"""
import pandas as pd

shop = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Rice", "Oil", "Sugar", "Tea", "Soap"],
    "Category": ["Grocery", "Grocery", "Grocery", "Beverage", "Personal Care"],
    "Price": [60, 150, 45, 300, 40],
    "Quantity": [200, 100, 150, 30, 250],
}
df = pd.DataFrame(shop)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print("\nProducts with sales > 10,000:\n", df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:\n", df.loc[df["Total_Sales"].idxmax()])
print("\nAverage sales:", df["Total_Sales"].mean())
