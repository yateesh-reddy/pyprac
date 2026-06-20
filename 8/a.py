# shapes.py
def area_circle(r):
    return 3.14 * r * r


def area_rectangle(l, b):
    return l * b


def area_square(s):
    return s * s


# main.py
import shapes

print(shapes.area_circle(5))
print(shapes.area_rectangle(4, 6))
print(shapes.area_square(4))
