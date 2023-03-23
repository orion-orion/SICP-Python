def sqrt(x):
    def is_good_enough(guess):
        return abs(guess**2 - x) < 0.001

    def improve(guess):
        return (guess + x/guess)/2

    def sqrt_iter(guess):
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))
        
    return  sqrt_iter(1.0)

print(sqrt(2))