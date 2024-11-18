import numpy as np

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  

element = array_3d[1, 0, 1] # Element at (width, Row, Column)

slice_3d = array_3d[:, 0, :]

print('Element at (1, 0, 1): ', element)
print('Slice 3d Array:\n ', slice_3d)
print("------------------------")
print(array_3d)