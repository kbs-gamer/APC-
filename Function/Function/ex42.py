# Exercise 42: Use filter() with lambda to identify prime numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20, 23, 25, 29]

# A number n > 1 is prime if no number in 2..int(sqrt(n))+1 divides it
is_prime_lambda = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

prime_numbers = list(filter(is_prime_lambda, numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
