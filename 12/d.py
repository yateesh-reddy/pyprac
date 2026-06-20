# shapes.py

def circle(r):
    return 3.14 * r * r

def rectangle(l, b):
    return l * b

def square(s):
    return s * s

# main.py

import shapes

print(shapes.circle(5))
print(shapes.rectangle(4, 6))
print(shapes.square(4))