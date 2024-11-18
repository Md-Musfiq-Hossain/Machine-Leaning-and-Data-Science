import numpy as np

array = np. array([1, 2, 3, 4, 5])

clipped_array = np.clip(array, 2, 4)

print('Original Array: ', array)
print('Clipped Array: ', clipped_array)