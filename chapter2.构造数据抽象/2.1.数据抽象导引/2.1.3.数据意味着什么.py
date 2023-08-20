def cons(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
        else:
            raise ValueError("Argument not 0 or 1 -- CONS", m)
    return dispatch


def car(z):
    return z(0)


def cdr(z):
    return z(1)


x = cons(1, 2)
print(car(x), cdr(x))  # 1 2


def cons(x, y):
    return lambda m: m(x, y)


def car(z):
    return z(lambda p, q: p)


def cdr(z):
    return z(lambda p, q: q)


x = cons(1, 2)
print(car(x), cdr(x))  # 1 2


def zero(f): return (lambda x: x)


def one(f): return lambda x: f(x)


def two(f): return lambda x: f(f(x))


def add_1(n):
    return lambda f: (lambda x: (f(n(f)(x))))


def inc(x):
    return x + 1


print(zero(inc)(0))  # 0
print(one(inc)(0))  # 1
print(two(inc)(0))  # 2
print(add_1(one)(inc)(0))  # 2
