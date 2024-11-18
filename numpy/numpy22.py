import numpy as np


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

lower_triangle = np.tril(matrix)

print('Lower Triangle of the Matrix:\n', lower_triangle)