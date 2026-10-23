# 21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.

squares = {n: n**2 for n in range(1, 11)}

print("Numbers 1 to 10 and their squares:")
for num, sq in squares.items():
    print(f"  {num}^2 = {sq}")
