# prep_data.py
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder

# 1. Load the dataset using Pandas
print("--- 1. Loading Dataset ---")
df = pd.read_csv("dataset2.csv")
print(df)
print("\nMissing values before cleaning:\n", df.isnull().sum())

# Separate features (X) and target (y)
X = df[["sqrft", "rooms", "condition"]]
y = df["target_price"]

# Separate numerical and categorical columns for processing
num_cols = ["sqrft", "rooms"]
cat_cols = ["condition"]

# 2. Handle missing values (Imputation)
print("\n--- 2. Handling Missing Values ---")
# Numerical Imputer: replace missing with column mean
num_imputer = SimpleImputer(strategy="mean")
X_num_imputed = num_imputer.fit_transform(X[num_cols])

# Categorical Imputer: replace missing with the most frequent value (mode)
cat_imputer = SimpleImputer(strategy="most_frequent")
X_cat_imputed = cat_imputer.fit_transform(X[cat_cols])
print("Imputed Categorical Feature:\n", X_cat_imputed)

# 3. Label Encoding (Using OrdinalEncoder for features)
print("\n--- 3. Label Encoding Categorical Data ---")
# We use OrdinalEncoder here as it safely handles 2D feature arrays.
# It converts ['Average', 'Good', 'Poor'] to integers like [0, 1, 2]
# Pass it as a list of lists (one list per categorical column).
condition_hierarchy = ['Poor', 'Average', 'Good']
label_encoder = OrdinalEncoder(categories=[condition_hierarchy])
X_cat_encoded = label_encoder.fit_transform(X_cat_imputed)
print("Label Encoded Categories:\n", X_cat_encoded)
print("Categories mapped to integers:", label_encoder.categories_)

# 4. Scale Numerical Features (MinMaxScaler)
print("\n--- 4. Min-Max Scaling Numerical Features ---")
# MinMaxScaler squeezes all data precisely into a 0 to 1 range
min_max_scaler = MinMaxScaler()
X_num_scaled = min_max_scaler.fit_transform(X_num_imputed)
print("Min-Max Scaled Numerical Array:\n", X_num_scaled)

# 5. Combine Processed Features
print("\n--- 5. Final Processed Dataset ---")
# Concatenate the scaled numerical features and encoded categorical features horizontally
X_final = np.hstack((X_num_scaled, X_cat_encoded))
print(np.round(X_final, 3)) # Rounded for easier reading