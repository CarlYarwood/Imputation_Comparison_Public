import numpy as np
import random as rand
from matplotlib import pyplot as plt
rand.seed(490509)
x_vals = np.arange(0, 10*np.pi, .1 )
y_vals = np.sin(x_vals)
outlier_1 = rand.randint(1,100)
outlier_2 = rand.randint(1,100)
y_vals[outlier_1] += 5
y_vals[outlier_2] -= 5
mu = np.sum(y_vals)/len(y_vals)
s = np.sqrt(np.sum(np.square([y - mu for y in y_vals]))/(len(y_vals)-1))
upper_bound = mu + (3 * s)
lower_bound = mu - (3 * s)
data = np.array([x_vals, y_vals])
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8,8))
axs[0].plot(data[0], data[1])
axs[0].set_title("With Outliers")
outlier_indexs = []
for i in range(len(data[0])):
    if data[1][i] > upper_bound or data[1][i] < lower_bound:
        print("in if")
        outlier_indexs.append(i)
print(outlier_indexs)
new_x = np.delete(data[0], outlier_indexs)
new_y = np.delete(data[1], outlier_indexs)
data_no_outliers = np.array([new_x, new_y])
axs[1].plot(data_no_outliers[0], data_no_outliers[1])
axs[1].set_title("Without Outliers")
plt.show()
