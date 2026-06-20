n = int(input("Enter n: "))

s = 0
for i in range(1, n + 1, 2):
    s += i

print("Sum =", s)

# OR
n = int(input())
print(sum(range(1, n + 1, 2)))