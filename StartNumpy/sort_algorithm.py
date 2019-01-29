# -*- coding: utf-8 -*-
import numpy as np
from timeit import timeit


def selection_sort(x):
    for i in range(np.size(x)):
        swap = i + np.argmax(x[i:])
        x[i], x[swap] = x[swap], x[i]
    return x


x = np.array([2, 1, 3, 5, 4])
print(selection_sort(x))

x.sort()
np.random.rand()