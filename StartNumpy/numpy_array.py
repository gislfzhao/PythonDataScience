# -*- coding: utf-8 -*-
import numpy as np

np.random.seed(0)

x1 = np.random.randint(10, size=3)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print(x1)
print(x2)
print(x3)

print(x3.ndim, x3.shape, x3.size, x3.dtype, x3.itemsize, x3.nbytes)

grid = np.arange(0, 10)
print(grid)
grid2 = grid.reshape((2, 5))
print(grid2)
grid2[0, 0] = 100
print(grid2)
print(grid)

