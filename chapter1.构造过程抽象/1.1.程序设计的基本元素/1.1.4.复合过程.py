def square(x):
    return x * x


print(square(21))  # 441
print(square(2 + 5))  # 49
print(square(square(3)))  # 81


def sum_of_squares(x, y):
    return square(x) + square(y)


print(sum_of_squares(3, 4))  # 25


def f(a):
    return sum_of_squares(a + 1, a * 2)


print(f(5))  # 136
