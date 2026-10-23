# Exercise 35: Lambda function that returns True if a number is even and False otherwise

is_even = lambda n: n % 2 == 0

numbers = [10, 15, 22, 33, 40]

for n in numbers:
    print(f"Is {n} even? -> {is_even(n)}")
