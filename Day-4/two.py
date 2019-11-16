# x + 3y + 5z = 10

# 2x + 5y + z = 8

# 2x + 3y + 8z = 3

from scipy import linalg
import numpy as np

a = np.array([[ 1, 3, 5], [2, 5, 1], [2, 3, 8]])
b = np.array([10, 8, 3])

x = linalg.solve(a, b)
print(x)
