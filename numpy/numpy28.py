import numpy as np

array = np.array([10, 15, 20, 25, 30])

result = np.where(array > 2, 0, array)

print('Array with Values Greater than 20 replaced with 0: ', result)