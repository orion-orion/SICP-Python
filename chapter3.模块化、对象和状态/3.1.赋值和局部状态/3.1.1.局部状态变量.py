balance = 100
def withdraw(amount):
    global balance
    if balance > amount:
        balance = balance - amount
        return balance
    else: 
        return "Insufficient funds"

print(withdraw(25)) # 70
print(withdraw(25)) # 50
print(withdraw(60)) # "In sufficient funds"
print(withdraw(15)) # 35


def new_withdraw():
    balance = 100
    def inner(amount):
        nonlocal balance
        if balance > amount:
            balance = balance - amount
            return balance
        else:
            return "Insufficient funds"
    return inner

W = new_withdraw()
print(W(25)) # 70
print(W(25)) # 50
print(W(60)) # "In sufficient funds"
print(W(15)) # 35


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
W2 = make_withdraw(100)
print(W1(50)) # 50
print(W2(70)) # 30
print(W2(40)) # Insufficient funds
print(W1(40)) # 10


def make_account(balance):
    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance = balance - amount
            return balance
        else:
            return "In sufficient funds"
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance
    def dispatch(m):
        nonlocal balance
        if m == "withdraw":
            return withdraw
        if m == "deposit":
            return deposit
        else:
            raise ValueError("Unkown request -- MAKE_ACOUNT %s" % m)
    return dispatch

acc = make_account(100)
print(acc("withdraw")(50)) # 50
print(acc("withdraw")(60)) # In sufficient funds
print(acc("deposit")(40)) # 90
print(acc("withdraw")(60)) # 30

acc2 = make_account(100)


def make_accumulator(sum_value):
    def accumulator(number):
        nonlocal sum_value
        sum_value += number
        return sum_value
    return accumulator

A =  make_accumulator(5)
print(A(10)) # 15
print(A(10)) # 25






            
    








    

















