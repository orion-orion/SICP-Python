def sum_odd_squares(tree):
    if not tree:
        return 0
    elif isinstance(tree, int):
        if tree % 2 == 1:
            return tree**2
        else:
            return 0
    else:
        return sum_odd_squares(tree[0]) + sum_odd_squares(tree[1:])

print(sum_odd_squares([[1, 2], 3, 4])) # 10


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def even_fibs(n):  # 枚举从0到n的整数
    def next(k):
        if k > n:
            return []
        else:
            f = fib(k)  # 对每个整数计算其fib
            if f % 2 == 0:  # 过滤结果，选出其中偶数
                return [f] + next(k + 1)  # 累积结果
            else:
                return next(k+1)
    return next(0)
print(even_fibs(5)) # [0, 2] (即[0 1 1 2 3 5]中的偶数为[0, 2])


def con(x, y):
    # y规定为int，x可以为int或list
    if isinstance(x, int):
        return [x] + [y]
    else:
        return x + [y]
    

def my_map(proc, sequence):
    if not sequence:
        return []
    else:
        return [proc(sequence[0])] + my_map(proc, sequence[1:])

print(my_map(lambda x: x**2, [1, 2, 3, 4, 5]))
# [1, 4, 9, 16, 25]


def my_filter(predicate, sequence):
    if not sequence:
        return []
    elif predicate(sequence[0]):
        return [sequence[0]] + my_filter(predicate, sequence[1:])
    else:
        return my_filter(predicate, sequence[1:])

print(my_filter(lambda x: x % 2, [1, 2, 3, 4, 5]))
# [1, 3, 5]


def my_reduce(op, sequence):
    if sequence[-1] and not sequence[:-1]:
        return sequence[-1]
    else:
        return op(my_reduce(op, sequence[:-1]), sequence[-1])

from operator import add, mul

print(my_reduce(add, [1, 2, 3, 4, 5])) # 15
print(my_reduce(mul, [1, 2, 3, 4, 5])) # 120
print(my_reduce(con, [1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]


def enumerate_interval(low, high):
    if low > high:
        return []
    else:
        return [low] + enumerate_interval(low + 1, high)

print(enumerate_interval(0, 5)) # [0, 1, 2, 3, 4, 5]


# 枚举一棵树所有的树叶：
def enumerate_tree(tree):
    if not tree:
        return []
    elif isinstance(tree, int):
        return [tree]
    else:
        return enumerate_tree(tree[0]) + enumerate_tree(tree[1:])

print(enumerate_tree([[1, 2], 3, 4])) # [1, 2, 3, 4]


from functools import reduce
def sum_odd_squares(tree):
    return reduce(add,
                  map(lambda x: x**2,
                      filter(lambda x: x % 2,
                             enumerate_tree(tree))))

print(sum_odd_squares([1, 2, 3, 4, 5])) # 35


def even_fibs(n):
    return reduce(con,
                  filter(lambda x: not x % 2,
                         map(fib,
                             enumerate_interval(0, n))))

print(even_fibs(5)) #[0, 2]


def list_fib_squares(n):
    return reduce(con,
                  map(lambda x: x**2,
                      map(fib,
                          enumerate_interval(0, n))))

print(list_fib_squares(5)) # [0, 1, 1, 4, 9, 25]


def product_of_squares_of_odd_elements_sequence(sequence):
    return reduce(mul,
                  map(lambda x: x**2,
                      filter(lambda x: x % 2, sequence)))

print(product_of_squares_of_odd_elements_sequence([1, 2, 3, 4, 5])) # 225


# def salary_of_hightest_paid_programmer(records):
#     return reduce(max,
#                   map(salary,
#                       filter(is_programmer, records)))
