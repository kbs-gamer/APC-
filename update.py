arr = [10, 20, 30, 40]

old = int(input("Enter old value: "))
new = int(input("Enter new value: "))

i = arr.index(old)

arr[i] = new

print(arr)