# Exercise 44: Use filter() and lambda to find numbers greater than 50

numbers = [15, 52, 38, 99, 45, 60, 50, 75, 12, 88]

greater_than_50 = list(filter(lambda x: x > 50, numbers))

print("Original list:", numbers)
print("Numbers greater than 50:", greater_than_50)
