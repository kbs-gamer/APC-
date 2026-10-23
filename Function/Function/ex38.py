# Exercise 38: Use map() and a lambda function to generate squares of elements in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original list:", numbers)
print("Squared list:", squared_numbers)
