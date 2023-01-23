def attach_tag(type_tag, contents):
    return [type_tag, contents]

def type_tag(datum):
    if isinstance(datum, list):
        return datum[0]
    else:
        raise ValueError("Bad tagged dataum -- TYPE-TAG", datum)

def contents(datum):
    if isinstance(datum, list):
        return datum[1]
    else:
        raise ValueError("Bad tagged dataum -- CONTENTS", datum)

def is_rectangular(z):
    return type_tag(z) == "rectangular"

def is_polar(z):
    return type_tag(z) == "polar"

def real_part_rectangular(z):
    return z[0]

def imag_part_rectangular(z):
    return z[1]

import math
def magnitude_rectangular(z):
    return math.sqrt(real_part_rectangular(z)**2 +
                     imag_part_rectangular(z)**2)

def angle_rectangular(z):
    return math.atan2(imag_part_rectangular(z),
                      real_part_rectangular(z))
    
def make_from_real_imag_rectangular(x, y):
    return attach_tag("rectangular", [x, y])

def make_from_mag_ang_rectangular(r, a):
    return attach_tag("rectangular", [r * math.cos(a), r * math.sin(a)])

def real_part_polar(z):
    return magnitude_polar(z) * math.cos(angle_polar(z))

def imag_part_polar(z):
    return magnitude_polar(z) * math.sin(angle_polar(z))

def magnitude_polar(z):
    return z[0]

def angle_polar(z):
    return z[1]

def make_from_real_imag_polar(x, y):
     return attach_tag("polar",
                       [math.sqrt(x**2 + y**2),
                        math.atan2(y, x)])

def make_from_mag_ang_polar(r, a):
    return attach_tag("polar", [r, a])                    

def real_part(z):
    if is_rectangular(z):
        return real_part_rectangular(contents(z))
    elif is_polar(z):
        return real_part_polar(contents(z))
    else:
        raise ValueError("Unknown type -- REAL-PART", z)
    
def imag_part(z):
    if is_rectangular(z):
        return imag_part_rectangular(contents(z))
    elif is_polar(z):
        return imag_part_polar(contents(z))
    else:
        raise ValueError("Unknown type -- IMAG-PART", z)

def magnitude(z):
    if is_rectangular(z):
        return magnitude_rectangular(contents(z))
    elif is_polar(z):
        return magnitude_polar(contents(z))
    else:
        raise ValueError("Unknown type -- MAGNITUDE", z)
    
def angle(z):
    if is_rectangular(z):
        return angle_rectangular(contents(z))
    elif is_polar(z):
        return angle_polar(contents(z))
    else:
        raise ValueError("Unknown type -- ANGLE", z)

# add-complex是通用型的，对任何表示都能工作
def add_complex(z1, z2):
    return make_from_real_imag(real_part(z1) + real_part(z2),
                               imag_part(z1) + imag_part(z2))

def make_from_real_imag(x, y):
    # 手头有实部和虚部时，构造函数的返回采用直角坐标表示
    return make_from_real_imag_rectangular(x, y)

def make_from_mag_angle(r, a):
    # 手头有模和幅角时，构造函数的返回采用极坐标表示
    return make_from_mag_ang_polar(r, a)


complex_1  = make_from_mag_ang_polar(1, math.pi/6) # (1, pi/6)
complex_2  = make_from_mag_ang_polar(1, math.pi/3) # (1, pi/3)

print(add_complex(complex_1, complex_2)) 
# ['rectangular', [1.3660254037844388, 1.3660254037844386]], 对应(sqrt(3)/2 + 1/2, sqrt(3)/2 + 1/2)
