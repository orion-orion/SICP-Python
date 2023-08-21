import math


# def square(x):
#     return x * x


def square(x):
    return math.exp(double(math.log(x)))


def double(x):
    return x + x


print(square(2))  # 4.0


# def sqrt(x):
#     def is_good_enough(guess, x):
#         return abs(guess**2 - x) < 0.001

#     def improve(guess, x):
#         return average(guess, x / guess)

#     def average(x, y):
#         return (x + y) / 2

#     def sqrt_iter(guess, x):
#         if is_good_enough(guess, x):
#             return guess
#         else:
#             return sqrt_iter(improve(guess, x), x)
#     return sqrt_iter(1.0, x)


def sqrt(x):
    def is_good_enough(guess):
        return abs(guess**2 - x) < 0.001

    def improve(guess):
        return average(guess, x / guess)

    def average(x, y):
        return (x + y) / 2

    def sqrt_iter(guess):
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))
    return sqrt_iter(1.0)


print(sqrt(9))  # 3.00009155413138
print(sqrt(100 + 37))  # 11.704699917758145
print(sqrt(sqrt(2) + sqrt(3)))  # 1.7739279023207892
print(sqrt(1000)**2)  # 1000.000369924366
