import math


def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))


def sub_rat(x, y):
    return make_rat(numer(x) * denom(y) - numer(y) * denom(x),
                    denom(x) * denom(y))


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def div_rat(x, y):
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))


def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


# def make_rat(n, d):
#     return [n, d]


def make_rat(n, d):
    g = math.gcd(n, d)
    return [n // g, d // g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def print_rat(x):
    print("%d/%d" % (numer(x), denom(x)))


one_half = make_rat(1, 2)
print_rat(one_half)  # 1/2

one_third = make_rat(1, 3)

print_rat(add_rat(one_half, one_third))  # 5/6
print_rat(mul_rat(one_half, one_third))  # 1/6
print_rat(add_rat(one_third, one_third))  # 2/3
