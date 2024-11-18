import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

array[array % 2 == 0] = -1

print ('Array after conditional Indexing: ', array)