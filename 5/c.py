import math

a, b, c = map(int, input().split())

d = b*b - 4*a*c

r1 = (-b + math.sqrt(d)) / (2*a)
r2 = (-b - math.sqrt(d)) / (2*a)

print(r1, r2)