import math

a, b, c = map(float, input().split())

d = b * b - 4 * a * c

r1 = (-b + math.sqrt(d)) / (2 * a)
r2 = (-b - math.sqrt(d)) / (2 * a)

print("Roots:", r1, r2)
