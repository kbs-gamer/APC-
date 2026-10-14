def largest(numbers):
    large = numbers[0]

    for i in numbers:
        if i > large:
            large = i

    return large


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Largest number =", largest(numbers))