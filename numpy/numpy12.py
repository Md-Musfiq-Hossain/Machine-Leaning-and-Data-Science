import numpy as np
array = np.array([1, 2, 3, 4, 5, 6])

even_numbers = array[array % 2 == 0]

print("Orginal Array: ", array)
print('Even Number: ', even_numbers)