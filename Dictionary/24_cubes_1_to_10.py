# 24. Create a dictionary containing integers from 1 to 10 and their cubes.

cubes = {n: n**3 for n in range(1, 11)}

print("Integers 1 to 10 and their cubes:")
for num, cb in cubes.items():
    print(f"  {num}^3 = {cb}")
