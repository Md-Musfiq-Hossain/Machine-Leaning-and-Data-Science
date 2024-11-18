import numpy as np

x = np.array ([1, 2, 3])
y = np.array ([4, 5])


x, y = np.meshgrid(x, y)
indices = np.vstack([x.ravel(), y.ravel()])

print('Indices for Meshgrid Advance Indencing:\n ', indices)

print("------------------------")

print(x)
print("------------------------")

print(y)