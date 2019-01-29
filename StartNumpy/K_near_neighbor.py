# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


X = np.random.rand(10, 2)

differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
print(differences.shape)

sq_differences = differences ** 2
print(sq_differences.shape)

# 最末尾元素聚合
dist_sq = sq_differences.sum(axis=-1)
print(dist_sq)

# print(dist_sq)

print(dist_sq.diagonal())

# axis=1 行
nearest = np.argsort(dist_sq, axis=1)
# print(nearest)

# 将每个点与其最近的两个邻接点连接起来
K = 1
nearest2 = np.argpartition(dist_sq, K+1, axis=1)
plt.scatter(X[:, 0], X[:, 1], s=100)

for i in range(X.shape[0]):
    print(nearest2[i, 1: K + 1])
    for j in nearest2[i, 1: K + 1]:
        # 画一条从X[i]到X[j]的线段
        plt.plot(*zip(X[j], X[i]), color='black')
plt.show()
