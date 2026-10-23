# Exercise 40: Use map() and lambda to sum corresponding elements of two lists

list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]

summed_list = list(map(lambda a, b: a + b, list1, list2))

print("List 1:", list1)
print("List 2:", list2)
print("Sum of corresponding elements:", summed_list)
