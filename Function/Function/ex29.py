def binary_search(numbers, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == key:
        return mid

    elif key < numbers[mid]:
        return binary_search(numbers, key, low, mid - 1)

    else:
        return binary_search(numbers, key, mid + 1, high)


numbers = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Enter number to search: "))

result = binary_search(numbers, key, 0, len(numbers) - 1)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")