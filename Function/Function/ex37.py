# Exercise 37: Lambda function to calculate simple interest using principal, rate, and time

simple_interest = lambda p, r, t: (p * r * t) / 100

principal = 10000
rate = 7.5
time = 3

si = simple_interest(principal, rate, time)
print(f"Principal: Rs. {principal}, Rate: {rate}%, Time: {time} years")
print(f"Simple Interest: Rs. {si:.2f}")
print(f"Total Amount: Rs. {(principal + si):.2f}")
