import time


def expt(b, n):
    if n == 0:
        return 1
    else:
        return b * expt(b, n - 1)


print(expt(2, 3))  # 8


def expt(b, n):
    return expt_iter(b, n, 1)


def expt_iter(b, counter, product):
    if counter == 0:
        return product
    else:
        return expt_iter(b, counter - 1, b * product)


print(expt(2, 3))  # 8


def fast_expt(b, n):
    if n == 0:
        return 1
    elif is_even(n):
        return fast_expt(b, n/2)**2
    else:
        return b * fast_expt(b, n - 1)


def is_even(n):
    return n % 2 == 0


print(fast_expt(2, 5))  # 32


def fast_expt(b, n):
    return fast_expt_iter(b, n, 1)


def fast_expt_iter(b, counter, a):
    if counter == 0:
        return a
    elif is_even(counter):
        return fast_expt_iter(b, counter//2, a**2)
    else:
        return fast_expt_iter(b, counter - 1, a * b)


print(fast_expt(2, 5))  # 32


def mul(a, b):
    if b == 0:
        return 0
    else:
        return a + mul(a, b - 1)


print(mul(2, 3))  # 6


def fast_mul(a, b):
    if b == 0:
        return 0
    elif is_even(b):
        return fast_mul(double(a), halve(b))
    else:
        return a + fast_mul(a, b - 1)


def double(n):
    return n * 2


def halve(n):
    return n // 2


print(fast_mul(2, 3))  # 6


def fast_mul(a, b):
    return fast_mul_iter(a, b, 0)


def fast_mul_iter(a, counter, c):
    if counter == 0:
        return c
    elif is_even(counter):
        return fast_mul_iter(a, halve(counter), double(c))
    else:
        return fast_mul_iter(a, counter - 1, a + c)


print(fast_mul(2, 3))  # 6


def fib(n):
    return fib_iter(n)


def fib_iter(n):
    a, b = 1, 0
    for _ in range(n):
        temp = a
        a = a + b
        b = temp
    return b


def fast_fib(n):
    return fast_fib_iter(1, 0, 0, 1, n)


def fast_fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    elif is_even(count):
        return fast_fib_iter(
            a, b,
            p**2 + q**2,
            q**2 + 2 * p * q,
            count // 2
        )
    else:
        return fast_fib_iter(b * q + a * q + a * p,
                             b * p + a * q,
                             p, q, count - 1)


begin = time.time()
print(fib(5))  # 5
ans1 = fib(1000000)
end = time.time()
print("Time fib consumed: %.4f" % (end - begin))  # 11.8982

begin = time.time()
print(fast_fib(5))  # 5
ans2 = fast_fib(1000000)
end = time.time()
if ans1 == ans2:
    print("Answer correct!")
print("Time fast fib consumed: %.4f" % (end - begin))  # 0.1696
