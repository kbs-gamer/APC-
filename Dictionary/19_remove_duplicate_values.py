# 19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.

original_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

seen_values = set()
unique_val_dict = {}

for k, v in original_dict.items():
    if v not in seen_values:
        unique_val_dict[k] = v
        seen_values.add(v)

print("Original Dictionary (with duplicate values):", original_dict)
print("Dictionary after removing duplicate values:", unique_val_dict)
