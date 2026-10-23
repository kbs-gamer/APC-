# 23. Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 2, 1]

frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1

print("Number List:", numbers)
print("Unique Numbers and Frequencies:")
for n, count in frequency.items():
    print(f"  {n}: {count} times")
