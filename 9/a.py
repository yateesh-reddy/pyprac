p = float(input("Principal: "))
r = float(input("Rate: "))
t = int(input("Periods: "))

a = p * (1 + r / 100) ** t
ci = a - p

print("Compound Interest =", ci)