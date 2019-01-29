# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.randn(100)    # 满足正态分布的数组

# 手动计算直方图
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# 为每一个x找到合适的区间
i = np.searchsorted(bins, x)
print(i)

# 为每个区间加上1
np.add.at(counts, i, 1)
print(counts)

# plt.plot(bins, counts, linestyle='steps')
# plt.show()

plt.hist(x, bins, histtype='step')
# plt.show()
print(bins)
counts, edges = np.histogram(x, bins)
print(counts, edges)

