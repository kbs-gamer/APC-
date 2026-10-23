# 32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.

def find_two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (complement, num), (seen[complement], i)
        seen[num] = i
    return None

numbers = [2, 7, 11, 15, 3, 6]
target = 9

result = find_two_sum(numbers, target)
print(f"Numbers: {numbers}")
print(f"Target: {target}")
if result:
    vals, indices = result
    print(f"Found pair: {vals[0]} + {vals[1]} = {target} (at indices {indices[0]}, {indices[1]})")
else:
    print("No two numbers sum to target.")
