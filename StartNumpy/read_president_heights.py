# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
print("Mean height: ", heights.mean())
print("Max height: ", heights.max())
print("Min height: ", heights.min())
print("Standard deviation: ", heights.std())

print("25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th percentile: ", np.percentile(heights, 75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()
