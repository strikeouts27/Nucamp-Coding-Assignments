def show_balance(balance):
    # eliminates the need for printing the balance.
    print("Your balance is:", balance)


def deposit(balance):
    # input always returns a string so you need to immedatiley typecast the outcome by redefining variable.
    amount = input("Enter amount to deposit:")
    amount = float(amount)  # always use float in case of decimals.
    return balance + amount


def withdraw(balance):
    amount = input("Enter amount to withdraw:")
    amount = float(amount)
    return balance - amount
    if float(amount) > balance:
        print("insufficent funds")
        return balance
    return balance - amount
    # incomplete portion WORK ON THIS!


def logout(name):
    print("goodbye", name + "!")  # same thing but subtracting.


# f string formatting def show_balance(balance)
# print(f'Your balance is ({balance!}))
# look up f string formatting.
