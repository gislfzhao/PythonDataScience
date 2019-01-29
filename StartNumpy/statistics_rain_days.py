# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254
# plt.hist(inches, 40)
# plt.show()
print("Number days without rain:", np.sum(inches == 0))
print("Number days with rain:", np.sum(inches != 0))
print("Rainy days with < 0.1 inches:", np.sum((inches > 0) & (inches < 0.2)))

rainy = inches > 0
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)

print(np.mean(inches[rainy]))
print(np.median(inches[summer]))