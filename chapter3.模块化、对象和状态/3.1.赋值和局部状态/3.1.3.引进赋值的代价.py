def make_simplified_withdraw(balance):
    def simplified_withdraw(amount):
        nonlocal balance
        balance = balance - amount
        return balance
    return simplified_withdraw

W = make_simplified_withdraw(25)
print(W(20)) # 5
print(W(10)) # -5


def make_decrementer(balance):
    return lambda amount: balance - amount

D = make_decrementer(25)
print(D(20)) # 5
print(D(10)) # 15

print(make_decrementer(25)(20)) # 5
print((lambda amount: 25 - amount)(20)) # 5

print(make_simplified_withdraw(25)(20)) # 5


D1 = make_decrementer(25)
D2 = make_decrementer(25)
print(D1(20)) # 5
print(D1(20)) # 5
print(D2(20)) # 5

W1 = make_simplified_withdraw(25)
W2 = make_simplified_withdraw(25)
print(W1(20)) # 5
print(W1(20)) # -15
print(W2(20)) # 5


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

peter_acc = make_account(100)
paul_acc = make_account(100)
peter_acc("withdraw")(10)
print(paul_acc("withdraw")(10)) # 90

peter_acc = make_account(100)
paul_acc = peter_acc
peter_acc("withdraw")(10)
print(paul_acc("withdraw")(10)) # 80


def factorial(n):
    def iter(product, counter):
        if counter > n:
            return product
        else:
            return iter(counter * product, counter + 1)
    return iter(1, 1)

print(factorial(4)) # 24


def factorial(n):
    product, counter = 1, 1
    def iter():
        nonlocal product, counter
        if counter > n:
            return product
        else:
            product = counter * product
            counter = counter + 1
            return iter()
    return iter()

print(factorial(4)) # 24


def factorial(n):
    product, counter = 1, 1
    def iter():
        nonlocal product, counter
        if counter > n:
            return product
        else:
            counter = counter + 1 # reverse order
            product = counter * product # reverse order
            return iter()
    return iter()

print(factorial(4)) # 120， Wrong!



