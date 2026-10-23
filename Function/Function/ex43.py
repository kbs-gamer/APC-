# Exercise 43: Use filter() and lambda to extract positive numbers from a list

numbers = [-15, 20, 0, -3, 45, -8, 12, -90, 7]

positive_numbers = list(filter(lambda x: x > 0, numbers))

print("Original list:", numbers)
print("Positive numbers:", positive_numbers)
