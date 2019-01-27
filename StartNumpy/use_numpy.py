# -*- coding: utf-8 -*-
import numpy as np

A = np.array([1, 2, 3])
print(type(A))

B = np.array([1, 2.0, 3, 4.1], dtype='float16')
print(B)

C = np.array([range(i, i + 3) for i in [2, 3, 5]])
print(C)

D = np.zeros(10, dtype=np.int)
print(D)

F = np.ones((3, 5), dtype=np.float32)
print(F)
E = np.full((3, 5), 3.14, dtype=np.float32)
print(E)

F = np.arange(0, 20, 2)
print(F)
print(F.dtype)

G = np.linspace(0, 1, 4)
print(G)

G = np.random.random((3, 3))
print(G)

G = np.random.randint(0, 10, (3, 3))
print(G)

G = np.random.normal(0, 1, (3, 3))
print(G)

G = np.eye(3)
print(G)

G = np.empty((3, 2))
print(G)
print(type(G))