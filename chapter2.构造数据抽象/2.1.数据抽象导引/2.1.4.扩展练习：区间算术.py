def add_interval(x, y):
    return make_interval(lower_bound(x) + lower_bound(y),
                         upper_bound(x) + upper_bound(y))


def sub_intercal(x, y):
    return make_interval(lower_bound(x) - upper_bound(y),
                         upper_bound(x) + lower_bound(y))


def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4),
                         max(p1, p2, p3, p4))


def div_interval(x, y):
    return mul_interval(x,
                        make_interval(1.0 / upper_bound(y),
                                      1.0 / lower_bound(y)))


def make_interval(a, b):
    return [a, b]


def lower_bound(x):
    return x[0]


def upper_bound(x):
    return x[1]


r1 = make_interval(6.12, 7.48)
r2 = make_interval(4.465, 4.935)


def par1(r1, r2):
    return div_interval(mul_interval(r1, r2),
                        add_interval(r1, r2))


def par2(r1, r2):
    one = make_interval(1, 1)
    return div_interval(one,
                        add_interval(div_interval(one, r1),
                                     div_interval(one, r2)))


print(par1(r1, r2))  # [2.201031010873943, 3.4873689182805854]
print(par2(r1, r2))  # [2.581558809636278, 2.97332259363673]
