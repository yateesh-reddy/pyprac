import numpy as np

m = int(input())
n = int(input())

a = np.array([list(map(int, input().split())) for _ in range(m)])

print(a.T)