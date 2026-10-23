# 22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.

even_squares = {n: n**2 for n in range(1, 21) if n % 2 == 0}

print("Even numbers from 1 to 20 and their squares:")
for num, sq in even_squares.items():
    print(f"  {num}^2 = {sq}")
