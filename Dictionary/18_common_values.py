# 18. Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {"x": 10, "y": 20, "z": 30, "w": 40}
dict2 = {"p": 20, "q": 40, "r": 50, "s": 60}

common_values = set(dict1.values()) & set(dict2.values())

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Common Values:", sorted(common_values))
