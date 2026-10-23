# 17. Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"c": 30, "d": 40, "e": 50, "f": 60}

common_keys = set(dict1.keys()) & set(dict2.keys())

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Common Keys:", sorted(common_keys))
