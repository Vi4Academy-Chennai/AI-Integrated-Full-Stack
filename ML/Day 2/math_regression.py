import numpy as np

feature1 = [1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000]
feature2 = [2, 3, 3, 4, 4, 5, 5, 5]
target_price = [180000, 220000, 260000, 290000, 310000, 350000, 390000, 420000]

# Construct X (adding intercept column of 1s)
X = np.column_stack((np.ones(len(feature1)), feature1, feature2))
Y = np.array(target_price).reshape(-1, 1)

# Computations
X_T = X.T
X_T_X = X_T.dot(X)
X_T_X_inv = np.linalg.inv(X_T_X)
X_T_Y = X_T.dot(Y)
beta = X_T_X_inv.dot(X_T_Y)

print("X:\n", X)
print("Y:\n", Y)
print("X_T_X:\n", X_T_X)
print("X_T_X_inv:\n", np.array2string(X_T_X_inv, formatter={'float_kind':lambda x: "%.5e" % x}))
print("X_T_Y:\n", X_T_Y)
print("Beta:\n", beta)