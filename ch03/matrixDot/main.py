import numpy as np

x = np.array([1, 2])
y = np.array([3, 4])
print(x.shape, y.shape, np.dot(x, y))

x = np.array([1, 2])
y = np.array([[1, 2], [3, 4]])
print(x.shape, y.shape, np.dot(x, y))

x = np.array([1, 2])
y = np.array([[1, 2, 3], [3, 4, 5]])
print(x.shape, y.shape, np.dot(x, y))