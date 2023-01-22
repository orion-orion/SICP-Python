def add_complex(z1, z2):
    return make_from_real_imag(real_part(z1) + real_part(z2), imag_part(z1) + imag_part(z2))

def sub_complex(z1, z2):
    return make_from_real_imag(real_part(z1) - real_part(z2), imag_part(z1) - imag_part(z2))

def mul_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) * magnitude(z2), angle(z1) + angle(z2))

def div_complex(z1, z2):
    return make_from_mag_ang(magnitude(z1) / magnitude(z2), angle(z1) - angle(z2))    

def real_part(z):
    return z[0]

def imag_part(z):
    return z[1]

def magnitude(z):
    return math.sqrt(real_part(z) ** 2 + imag_part(z) ** 2)

import math 
def angle(z):
    return math.atan2(imag_part(z), real_part(z))

def make_from_real_imag(x, y):
    return [x, y]

def make_from_mag_ang(r, a):
    return [r * math.cos(a), r * math.sin(a)]

complex_1 = make_from_real_imag(math.sqrt(3)/2, 1/2)

complex_2 = make_from_real_imag(1/2, math.sqrt(3)/2)

print(add_complex(complex_1, complex_2))
print(mul_complex(complex_1, complex_2))

 