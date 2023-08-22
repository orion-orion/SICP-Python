def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))  # 5


def fib(n):
    # f(1) f(0)
    return fib_iter(1, 0, n)


def fib_iter(a, b, count):
    # a: f(n+1), b: f(n)
    if count == 0:
        return b  # f(n)
    else:
        # Iterate `count` times in total to get `Fib(count)`
        return fib_iter(a + b, a, count - 1)


print(fib(5))  # 5


def count_change(amount):
    return cc(amount, 5)


def cc(amount, kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        return cc(amount, kinds_of_coins - 1) \
            + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)


def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 4:
        return 25
    elif kinds_of_coins == 5:
        return 50


print(count_change(100))  # 292


def f(n):
    if n < 3:
        return n
    else:
        return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)


print(f(5))  # 25


def f(n):
    # f(2) f(1) f(0)
    return f_iter(2, 1, 0, n)


def f_iter(a, b, c, count):
    # a: f(n+2), b: f(n+1), c: f(n)
    if count == 0:
        return c  # f(n)
    else:
        # Iterate `count` times in total to get `f(count)`
        return f_iter(a + 2 * b + 3 * c, a, b, count - 1)


print(f(5))  # 25


def pascal(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal(row - 1, col - 1) + pascal(row - 1, col)


print(pascal(0, 0))  # 1
print(pascal(1, 0))  # 1
print(pascal(1, 1))  # 1
print(pascal(4, 2))  # 6
