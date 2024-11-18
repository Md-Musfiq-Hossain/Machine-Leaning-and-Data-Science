import numpy as np

array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12]])

result = array_2d[::2,::2]

print('Advance Sliced Array with steps: \n ', result)