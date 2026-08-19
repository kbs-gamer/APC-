arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

position = int(input("Enter the position: "))
element = int(input("Enter the element to insert: "))

arr.insert(position, element)

print("Updated array:", arr)