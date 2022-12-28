def is_number(x):
    return isinstance(x, str) and x.isnumeric()

def is_variable(x):
    return isinstance(x, str) and x.isalpha()

def is_same_variable(v1, v2):
    return is_variable(v1) and is_variable(v2) and v1 == v2

# 和式就是第0个元素（下标从0开始）为符号为+的元组
def is_sum(x):
    return isinstance(x, tuple) and x[0] == "+"

# s的被加数是和式元组里的第1个元素（下标从0开始）
def addend(s):
    return s[1]

# s的加数是表达和式元组里的第2个元素（下标从0开始）
def augend(s):
    return s[2]

def eq_number(exp, num):
    return is_number(exp) and exp == num

# 构造起a1和a2的和式
# def make_sum(a1, a2):
#     return ("+", a1, a2)
def make_sum(a1, a2):
    if eq_number(a1, "0"):
        return a2
    elif eq_number(a2, "0"):
        return a1
    elif is_number(a1) and is_number(a2):
        return str(int(a1) + int(a2))
    else:
        return ("+", a1, a2)

# 乘式就是第0个元素（下标从0开始）为符号为*的元组
def is_product(x):
    return isinstance(x, tuple) and x[0] == "*"

# p的被乘数是表示乘式的元组里的第1个元素（下标从0开始）
def multiplier(p):
    return p[1]

# p的乘数是表达乘式的元组里的第2个元素（下标从0开始）
def multiplicand(p):
    return p[2]

# 构造起m1和m2的乘式
# def make_product(m1, m2):
#     return ("*", m1, m2)
def make_product(m1, m2):
    if eq_number(m1, "0") or eq_number(m2, "0"):
        return "0"
    elif eq_number(m1, "1"):
        return m2
    elif eq_number(m2, "1"):
        return m1
    elif is_number(m1) and is_number(m2):
        return str(int(m1) * int(m2))
    else:
        return ("*", m1, m2)

# 参数exp为表达式，var为欲求导的自变量
def deriv(exp, var):
    if is_number(exp):
        return "0"
    elif is_variable(exp):
        if is_same_variable(exp, var):
            return "1"
        else:
            return "0"
    elif is_sum(exp):
        return make_sum(deriv(addend(exp), var), \
                        deriv(augend(exp), var))
    elif is_product(exp):
        return make_sum(\
            make_product(multiplier(exp), \
                        deriv(multiplicand(exp), var)), \
            make_product(deriv(multiplier(exp), var), \
                        multiplicand(exp))
            )
    else:
        raise ValueError("unknown expression type") 
    

if __name__ == "__main__":
    
    # 输入为元组，默认已经完成了表达式解析
    print(deriv(("+", "x", "3"), "x")) # 1

    print(deriv(("*", "x", "y"), "x")) # y

    print(deriv(("*", ("*", "x", "y"), ("+", "x", "3")), "x"))
    # ('+', ('*', 'x', 'y'), ('*', 'y', ('+', 'x', '3')))
    # 对(x * y) * (x + 3)求导后得到  (x * y) + y * ( x + 3)
