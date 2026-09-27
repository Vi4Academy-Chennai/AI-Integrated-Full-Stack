# prep_data.py
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# 1. Load the dataset using Pandas
print("--- 1. Loading Dataset ---")
df = pd.read_csv("dataset.csv")
print(df)
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Separate features (X) and target (y)
X = df[["sqrft", "rooms", "house_type"]]
y = df["target_price"]

# Separate numerical and categorical columns for processing
num_cols = ["sqrft", "rooms"]
cat_cols = ["house_type"]

# 2. Handle missing values (Imputation)
print("\n--- 2. Handling Missing Values ---")
# Numerical Imputer: replace missing with column mean
num_imputer = SimpleImputer(strategy="mean")
X_num_imputed = num_imputer.fit_transform(X[num_cols])

# Categorical Imputer: replace missing with the most frequent value (mode)
cat_imputer = SimpleImputer(strategy="most_frequent")
X_cat_imputed = cat_imputer.fit_transform(X[cat_cols])
print("Imputed Categorical Feature:\n", X_cat_imputed)

# 3. Encode Categorical Data (One-Hot Encoding)
print("\n--- 3. Encoding Categorical Data ---")
encoder = OneHotEncoder(sparse_output=False) # sparse_output=False returns a standard array
X_cat_encoded = encoder.fit_transform(X_cat_imputed)
print("One-Hot Encoded Categories:\n", X_cat_encoded)
print("Category Names:", encoder.get_feature_names_out(cat_cols))

# 4. Scale Numerical Features (StandardScaler)
print("\n--- 4. Scaling Numerical Features ---")
# StandardScaler shifts data to mean=0 and variance=1. 
# (Alternatively, MinMaxScaler scales data between 0 and 1)
scaler = StandardScaler()
X_num_scaled = scaler.fit_transform(X_num_imputed)
print("Scaled Numerical Array:\n", X_num_scaled)

# 5. Combine Processed Features
print("\n--- 5. Final Processed Dataset ---")
# Concatenate the scaled numerical features and encoded categorical features horizontally
X_final = np.hstack((X_num_scaled, X_cat_encoded))
print(X_final)