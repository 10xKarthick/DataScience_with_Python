# x	+	y	+	z	=	6
#  	 	2y	+	5z	=	−4
# 2x	+	5y	−	z	=	27

from scipy import linalg
import numpy as np

a = np.array([[ 1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([6, -4, 27])

x = linalg.solve(a, b)
print(x)
