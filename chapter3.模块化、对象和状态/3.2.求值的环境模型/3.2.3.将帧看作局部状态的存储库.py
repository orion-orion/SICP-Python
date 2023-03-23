def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if balance > amount:
            balance = balance - amount
            return balance
        else:
            return "Insufficient funds"
    return withdraw

W1 = make_withdraw(100)
print(W1(50)) # 50

W2 = make_withdraw(100)
print(W2(50)) # 50