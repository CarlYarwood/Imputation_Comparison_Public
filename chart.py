import numpy as np
import random as rand
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
rand.seed(490509)
x_vals = np.array(range(1,1000), dtype=np.float32)
y_vals = np.array(range(1,1000), dtype=np.float32)
for i in range(len(x_vals)):
    if rand.random() < 0.26:
        y_vals[i] = np.nan
data = []
for i in range(len(x_vals)):
    data.append([x_vals[i], y_vals[i]])
mean_imp = SimpleImputer(missing_values=np.nan, strategy='mean')
knn_imp = KNNImputer(n_neighbors=2, weights="uniform")
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8,8))
mean_imp_data = mean_imp.fit_transform(data)
mean_x = [a[0] for a in mean_imp_data]
mean_y = [a[1] for a in mean_imp_data]
axs[0].scatter(mean_x, mean_y)
axs[0].set_title("Mean Imputation")
knn_imp_data = knn_imp.fit_transform(data)
knn_x = [a[0] for a in knn_imp_data]
knn_y = [a[1] for a in knn_imp_data]
axs[1].scatter(knn_x, knn_y)
axs[1].set_title("KNN Imputation")
plt.show()
