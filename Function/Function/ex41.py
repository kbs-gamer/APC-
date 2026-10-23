# Exercise 41: Use filter() and lambda to extract all even numbers from a list

numbers = [12, 17, 24, 33, 40, 55, 68, 71, 80, 99]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)
