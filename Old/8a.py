def area_square(s):
    return s*s

def area_rectangle(l, b):
    return l*b

def area_circle(r):
    return 3.14*r*r

import geometry

print(geometry.area_square(5))
print(geometry.area_rectangle(4, 6))
print(geometry.area_circle(3))