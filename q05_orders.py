"""Q5. Orders: Final Amount = Quantity x Price - Discount"""
import pandas as pd

orders = pd.DataFrame({
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Asha", "Bharat", "Chetan", "Deepa", "Esha"],
    "Product": ["Phone", "Shoes", "Watch", "Bag", "Laptop"],
    "Quantity": [1, 2, 1, 3, 1],
    "Price": [12000, 1500, 4500, 800, 45000],
    "Discount": [1000, 200, 500, 100, 5000],
})
orders["Final_Amount"] = orders["Quantity"] * orders["Price"] - orders["Discount"]

print("All orders:\n", orders)
print("\nOrders above 5,000:\n", orders[orders["Final_Amount"] > 5000])
print("\nHighest-value order:\n", orders.loc[orders["Final_Amount"].idxmax()])
print("\nAverage order value:", orders["Final_Amount"].mean())
