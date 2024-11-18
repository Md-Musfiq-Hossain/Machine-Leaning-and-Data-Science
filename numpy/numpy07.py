import numpy as np


array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])
indexed_elements = array_2d[rows, cols]

print('Indexed Elements:', indexed_elements)
