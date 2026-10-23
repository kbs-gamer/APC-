# Exercise 39: Use map() with lambda to calculate the cube of every element in a list

numbers = [1, 2, 3, 4, 5, 6]

cubed_numbers = list(map(lambda x: x ** 3, numbers))

print("Original list:", numbers)
print("Cubed list:", cubed_numbers)
