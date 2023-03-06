
def rand_update(x):
    a = int(pow(7, 5))
    b = 0
    m = int(pow(2, 31)) - 1
    return (a * x + b) % m

def make_rand(random_init):
    x = random_init
    def inner():
        nonlocal x
        x  = rand_update(x)
        return x
    return inner

# rand = make_rand(42)
# print(rand()) # 705894
# print(rand()) # 1126542223


rand = make_rand(42)
import math
def estimate_pi(trials):
    return math.sqrt(6 / monte_carlo(trials, cesaro_test))

def cesaro_test():
    return math.gcd(rand(), rand()) == 1

def monte_carlo(trials, experiment):
    def iter(trials_remaining, trials_passed):
        if trials_remaining == 0:
            return trials_passed / trials
        elif cesaro_test():
            return iter(trials_remaining - 1, trials_passed + 1)
        else:
            return iter(trials_remaining - 1, trials_passed)
    return iter(trials, 0)

print(estimate_pi(500)) # 3.178208630818641


random_init = 42
def estimate_pi(trials):
    return math.sqrt(6 / random_gcd_test(trials, random_init))

def random_gcd_test(trials, initial_x):
    def iter(trials_remaining, trials_passed, x):
        x1 = rand_update(x)
        x2 = rand_update(x1)
        if trials_remaining == 0:
            return trials_passed / trials
        elif math.gcd(x1, x2) == 1:
            return iter(trials_remaining - 1, trials_passed + 1, x2)
        else:
            return iter(trials_remaining - 1, trials_passed, x2)
    return iter(trials, 0, initial_x)

print(estimate_pi(500)) # 3.178208630818641