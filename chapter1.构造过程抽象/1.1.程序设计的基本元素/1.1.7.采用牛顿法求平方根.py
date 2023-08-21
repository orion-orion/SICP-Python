def sqrt_iter(guess, x):
    if is_good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)


def improve(guess, x):
    return average(guess, x / guess)


def average(x, y):
    return (x + y) / 2


def is_good_enough(guess, x):
    return abs(guess**2 - x) < 0.001


def sqrt(x):
    return sqrt_iter(1.0, x)


print(sqrt(9))  # 3.00009155413138
print(sqrt(100 + 37))  # 11.704699917758145
print(sqrt(sqrt(2) + sqrt(3)))  # 1.7739279023207892
print(sqrt(1000)**2)  # 1000.000369924366


def sqrt_iter2(guess, x):
    new_guess = improve(guess, x)
    if is_good_enough2(new_guess, guess):
        return new_guess
    else:
        return sqrt_iter2(new_guess, x)


def is_good_enough2(new_guess, guess):
    return abs((new_guess - guess) / guess) < 0.001


def sqrt2(x):
    return sqrt_iter2(1.0, x)


print(sqrt2(9))  # 3.000000001396984
print(sqrt2(100 + 37))  # 11.704699917758145
print(sqrt2(sqrt2(2) + sqrt2(3)))  # 1.7737712336472033
print(sqrt2(1000)**2)  # 1000.000369924366


def cbrt_iter(guess, x):
    if cb_is_good_enough(guess, x):
        return guess
    else:
        return cbrt_iter(cb_improve(guess, x), x)


def cb_improve(guess, x):
    return (x / guess**2 + 2 * guess) / 3


def cb_is_good_enough(guess, x):
    return abs(guess**3 - x) < 0.001


def cbrt(x):
    return cbrt_iter(1.0, x)


print(cbrt(9))  # 2.0801035255095734
print(cbrt(100 + 37))  # 5.15513673840956
print(cbrt(cbrt(2) + cbrt(3)))  # 1.3928519224798794
print(cbrt(1000)**2)  # 100.00000290531537
