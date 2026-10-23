# Exercise 32: Separate functions for arithmetic operations passed as arguments to calculate()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculate(operation_func, a, b):
    """Higher-order function that takes another function as an argument."""
    return operation_func(a, b)


num1 = 20
num2 = 5

print(f"Numbers: a = {num1}, b = {num2}")
print("Addition:", calculate(add, num1, num2))
print("Subtraction:", calculate(subtract, num1, num2))
print("Multiplication:", calculate(multiply, num1, num2))
print("Division:", calculate(divide, num1, num2))
