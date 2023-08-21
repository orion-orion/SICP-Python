def abs(x):
    if x > 0:
        return x
    elif x == 0:
        return 0
    elif x < 0:
        return -x


# def abs(x):
#     if x < 0:
#         return -x
#     else:
#         return x


print(abs(3))  # 3
print(abs(0))  # 0
print(abs(-3))  # 3


x = 8
print(x > 5 and x < 10)  # True
print(5 < x < 10)  # True
x = 4
print(x > 5 and x < 10)  # False
print(5 < x < 10)  # False


def ge(x, y):
    return x > y or x == y


# def ge(x, y):
#     return not x < y


x, y = 10, 5
print(ge(x, y))  # True
print(x >= y)  # True
