# Import required libraries
import numpy as np
from sklearn import preprocessing

# --------------------------
# Input Data
# --------------------------

input_data = np.array([
    [5.1, -2.9, 3.3],
    [-1.2, 7.8, -6.1],
    [3.9, 0.4, 1.2],
    [7.3, -9.9, -4.5]
])

print("Original Data:\n", input_data)

# --------------------------
# 1. Binarization
# --------------------------

binarizer = preprocessing.Binarizer(threshold=1.1)
data_binarized = binarizer.transform(input_data)

print("\nBinarized Data:\n", data_binarized)

# --------------------------
# 2. Min-Max Scaling (Range 1 to 2)
# --------------------------

minmax_scaler = preprocessing.MinMaxScaler(feature_range=(1, 2))
data_scaled_minmax = minmax_scaler.fit_transform(input_data)

print("\nMin-Max Scaled Data (Range 1 to 2):\n", data_scaled_minmax)

# --------------------------
# 3. L1 Normalization
# --------------------------

data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')

print("\nL1 Normalized Data:\n", data_normalized_l1)

# --------------------------
# 4. L2 Normalization
# --------------------------

data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')

print("\nL2 Normalized Data:\n", data_normalized_l2)
