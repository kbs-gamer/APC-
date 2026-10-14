"""Q10. Series: product names -> prices"""
import pandas as pd

price = pd.Series({"Laptop": 50000, "Mouse": 500, "Keyboard": 1200,
                   "Monitor": 8000, "Pen": 20})
print("All products and prices:\n", price)

new_price = price * 1.10          # increase every price by 10%
print("\nPrices after 10% increase:\n", new_price)

print("\nMost expensive product:", price.idxmax(), "->", price.max())
print("\nProducts costing more than 1,000:\n", price[price > 1000])
