def calculate(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return min(numbers), max(numbers), total, average


numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)