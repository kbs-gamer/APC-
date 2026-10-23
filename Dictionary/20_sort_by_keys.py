# 20. Create a dictionary and display its elements in ascending order of keys.

data = {
    "orange": 40,
    "apple": 100,
    "banana": 30,
    "mango": 80,
    "grapes": 50
}

sorted_by_keys = {k: data[k] for k in sorted(data.keys())}

print("Original Dictionary:", data)
print("Sorted in ascending order of keys:", sorted_by_keys)
