import numpy as np
import matplotlib
import pandas
import seaborn
from sklearn import preprocessing



#We imported a couple of packages. Let's create some sample data and add the line to this file:
input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, 4.3]])

data_standardized = preprocessing.scale(input_data)

print("input_data:", input_data)

print("")
print("Mean =", data_standardized.mean(axis=0))
print("Std deviation =", data_standardized.std(axis=0))


data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(input_data)

print("")
print("Min max scaled data =", data_scaled)


data_normalized = preprocessing.normalize(input_data, norm='l1')
print("\nL1 normalized data =", data_normalized)


data_binarized = preprocessing.Binarizer(threshold=1.4).transform(input_data)
print("\nBinarized data =", data_binarized)
