def add_complex(z1, z2):
    return make_from_real_imag(real_part(z1) + real_part(z2), imag_part(z1) + imag_part(z2))

def sub_complex(z1, z2):
    return make_from_real_imag(real_part(z1) - real_part(z2), imag_part(z1) - imag_part(z2))

def mul_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) * magnitude(z2), angle(z1) + angle(z2))

def div_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) / magnitude(z2), angle(z1) - angle(z2))    

import math 
def real_part(z):
    return z[0]

def imag_part(z):
    return z[1]

def magnitude(z):
    return math.sqrt(real_part(z) ** 2 + imag_part(z) ** 2)

def angle(z):
    return math.atan2(imag_part(z), real_part(z))

def make_from_real_imag(x, y):
    return [x, y]

def make_from_mag_ang(r, a):
    return [r * math.cos(a), r * math.sin(a)]

complex_1 = make_from_real_imag(math.sqrt(3)/2, 1/2) # (sqrt(3)/2, 1/2)

complex_2 = make_from_real_imag(1/2, math.sqrt(3)/2) # (1/2, sqrt(3)/2)

print(add_complex(complex_1, complex_2)) 
# [1.3660254037844386, 1.3660254037844386]， 对应(sqrt(3)/2 + 1/2, sqrt(3)/2 + 1/2)
print(mul_complex(complex_1, complex_2)) 
# [6.123233995736765e-17, 0.9999999999999998]，对应(0, 1)


def real_part(z):
    return magnitude(z) * math.cos(angle(z))

def imag_part(z):
    return magnitude(z) * math.sin(angle(z))

def magnitude(z):
    return z[0]

def angle(z):
    return z[1]

def make_from_real_imag(x, y):
    return [math.sqrt(x**2 + y**2), math.atan2(y, x)]

def make_from_mag_ang(r, a):
    return [r, a]

complex_1 = make_from_mag_ang(1, math.pi/6) # (1, pi/6)

complex_2 = make_from_mag_ang(1, math.pi/3) # (1, pi/3)

print(add_complex(complex_1, complex_2)) 
# [1.9318516525781366, 0.7853981633974483], 对应(sqrt(6) + sqrt(2))/2,  arctan(sqrt(3)/2 + 1/2, sqrt(3)/2 + 1/2))
print(mul_complex(complex_1, complex_2)) 
# [1, 1.5707963267948966] 对应(1, pi/2)





 