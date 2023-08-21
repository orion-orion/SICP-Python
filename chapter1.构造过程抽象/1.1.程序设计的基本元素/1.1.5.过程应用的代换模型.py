def square(x):
    return x * x


def sum_of_squares(x, y):
    return square(x) + square(y)


def f(a):
    return sum_of_squares(a + 1, a * 2)


print(f(5))  # 136
