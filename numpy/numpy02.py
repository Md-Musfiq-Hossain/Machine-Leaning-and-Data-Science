import numpy as np

array_2d = np.array([[1, 2, 3,], [4, 5, 6], [7, 8, 9]])

element = array_2d[1, 2]

row_slicing = array_2d[0, :]

column_slicing = array_2d[:, 1]

print('Element at (1, 2): ', element)
print('First Row: ', row_slicing)
print('Second Column: ', column_slicing)