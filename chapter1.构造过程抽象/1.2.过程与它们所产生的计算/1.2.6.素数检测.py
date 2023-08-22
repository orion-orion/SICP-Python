import random
import time


def smallest_divisor(n):
    return find_divisor(n, 2)


def find_divisor(n, test_divisor):
    if test_divisor**2 > n:
        return n
    elif is_divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def is_divides(a, b):
    return b % a == 0


def is_prime(n):
    return n == smallest_divisor(n)


begin = time.time()
print(is_prime(2))  # True
print(is_prime(4))  # False
print(is_prime(7))  # True
print(is_prime(561))  # False
print(is_prime(1105))  # False
print(is_prime(124233332145232144213415))  # False


def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif is_even(exp):
        return expmod(base, exp // 2, m)**2 % m
    else:
        return (base * expmod(base, exp - 1, m)) % m


def is_even(n):
    return n % 2 == 0


def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a
    return try_it(random.randint(1, n - 1))


def is_fast_prime(n, times):
    if times == 0:
        return True
    elif fermat_test(n):
        return is_fast_prime(n, times - 1)
    else:
        return False


print(is_fast_prime(2, 100))  # True
print(is_fast_prime(4, 100))  # False
print(is_fast_prime(7, 100))  # True
print(is_fast_prime(561, 100))  # True
print(is_fast_prime(1105, 100))  # True
print(is_fast_prime(124233332145232144213415, 100))  # False
