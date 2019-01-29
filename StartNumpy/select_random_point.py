# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

mean = [0, 0]
cov = [[1, 2], [2, 5]]  # 协方差矩阵，表示两个变量的相关程度
x = np.random.multivariate_normal(mean, cov, 100)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()
# print(x)
# print(x.shape)
# print(x.shape[0])
indices = np.random.choice(x.shape[0], 20, replace=False)
# print(indices)
selection = x[indices]
plt.scatter(x[:, 0], x[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', edgecolors='b', s=200)
plt.show()