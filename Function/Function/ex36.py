# Exercise 36: Lambda function to find the maximum of two numbers

find_max = lambda a, b: a if a > b else b

a, b = 45, 82
print(f"Numbers: a = {a}, b = {b}")
print("Maximum:", find_max(a, b))
