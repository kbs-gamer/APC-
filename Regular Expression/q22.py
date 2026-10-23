# Program 22: Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions
import re

invoice_text = """
Tax Invoice
Invoice Number: INV-2024-0042
Date of Issue: 15-08-2024
Due Date: 30/08/2024
Vendor: ABC Technologies Pvt Ltd

Item 1: Software License - Rs. 45,000.00
Item 2: Support Services - Rs. 5,500.50
Total Amount Payable: Rs. 50,500.50
Secondary Invoice Ref: INV-9871 on 01-09-2024 with total $1,200.00
"""

# Patterns
invoice_numbers = re.findall(r"\bINV-[A-Za-z0-9-]+\b", invoice_text)
dates = re.findall(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b", invoice_text)
amounts = re.findall(r"(?:Rs\.?|\$)\s*[\d,]+(?:\.\d{2})?", invoice_text)

print("Invoice Numbers Found:", invoice_numbers)
print("Dates Found:", dates)
print("Monetary Amounts Found:", amounts)
