def average(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total / len(numbers)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Average =", average(numbers))