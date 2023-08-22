def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))  # 720


def factorial(n):
    return fact_iter(1, 1, n)


def fact_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fact_iter(counter * product, counter + 1, max_count)


print(factorial(6))  # 720


def add1(a, b):
    if a == 0:
        return b
    else:
        return ((a - 1) + b) + 1


def add2(a, b):
    if a == 0:
        return b
    else:
        return (a - 1) + (b + 1)


print(add1(4, 5))  # 9
print(add2(4, 5))  # 9


def A(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1))


print(A(1, 10))  # 1024
print(A(2, 4))  # 65536
print(A(3, 3))  # 65536


def f(n):
    return A(0, n)


def g(n):
    return A(1, n)


def k(n):
    return 5 * n * n


print(f(5))  # 10
print(g(5))  # 32
print(k(5))  # 125
