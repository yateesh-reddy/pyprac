n = int(input("Enter order of matrix: "))

A = []
B = []

print("Enter Matrix A:")
for i in range(n):
    A.append(list(map(int, input().split())))

print("Enter Matrix B:")
for i in range(n):
    B.append(list(map(int, input().split())))

C = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

print("Result:")
for row in C:
    print(row)
