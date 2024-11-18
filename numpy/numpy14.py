import numpy as np


array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])


result = array_3d[..., 1]  # Selecting the second column in each 2D slice

print('Result using Ellipsis (...):\n', result)