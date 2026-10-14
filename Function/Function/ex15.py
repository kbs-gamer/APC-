def unique_elements(numbers):
    unique = []

    for i in numbers:
        if i not in unique:
            unique.append(i)

    return unique


numbers = list(map(int, input("Enter numbers: ").split()))

print("Unique elements =", unique_elements(numbers))