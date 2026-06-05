import numpy as np

m = int(input("Rows: "))
n = int(input("Columns: "))

A = np.random.randint(1, 10, (m, n))

print("Matrix:")
print(A)

print("Transpose:")
print(A.T)