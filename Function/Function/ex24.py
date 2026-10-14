balance = 0
history = []


def deposit(amount):
    global balance
    balance = balance + amount
    history.append("Deposited: " + str(amount))


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        history.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")


def show_balance():
    print("Balance =", balance)


def show_history():
    print("Transaction History:")
    for h in history:
        print(h)


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        withdraw(amount)

    elif choice == 3:
        show_balance()

    elif choice == 4:
        show_history()

    elif choice == 5:
        break

    else:
        print("Invalid choice")