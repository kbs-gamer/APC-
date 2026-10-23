# 16. Create two dictionaries and merge them into a single dictionary.

dict1 = {"apple": 50, "banana": 20, "cherry": 70}
dict2 = {"date": 90, "elderberry": 120, "banana": 25}

merged_dict = {**dict1, **dict2}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary (dict2 overrides common keys):")
print(merged_dict)
