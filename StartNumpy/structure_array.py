# -*- coding: utf-8 -*-
import numpy as np

x = np.zeros(4, dtype=np.int64)
print(x.dtype)

data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'),
                          'formats': ('U10', 'i4', 'f8')})
print(data)
name = ['A', 'B', 'C', 'D']
age = [13, 15, 12, 18]
weight = [60.3, 70.3, 50.1, 65.7]
data['name'] = name
data['age'] = age
data['weight'] = weight

print(data['name'])
print(data[data['age'] >= 15]['name'])

data_rec = data.view(np.recarray)
print(data_rec)
print(type(data_rec.age))


# A = np.zeros(2, dtype=[('hello', (int, 3)), ('world', np.void, 10)])
# print(A.dtype)
# print(A[0]['world'])
