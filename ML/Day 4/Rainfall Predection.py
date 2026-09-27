import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
import joblib

# 1. Load the Dataset
df = pd.read_csv("rainfall.csv")

# 2. Data Cleaning
# Drop rows where the target variable (ANNUAL) is missing
df_clean = df.dropna(subset=['ANNUAL']).copy()

# 3. Define Features (X) and Target (y)
# We are predicting total Annual rainfall using only early-year data and location
features = ['SUBDIVISION', 'JAN', 'FEB', 'MAR', 'APR', 'MAY']
target = 'ANNUAL'

X = df_clean[features]
y = df_clean[target]

# 4. Split the Data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Build Preprocessing Steps
numeric_features = ['JAN', 'FEB', 'MAR', 'APR', 'MAY']
categorical_features = ['SUBDIVISION']

# For numbers: Fill missing values with the mean, then Standardize
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# For text (Subdivision): Fill missing values with most frequent, then One-Hot Encode
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Combine both preprocessing steps into a ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 6. Create the Final Modeling Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 7. Train and Evaluate the Model
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Calculate metrics
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Root Mean Squared Error (RMSE): {rmse:.2f} mm")
print(f"R-squared (R2) Score: {r2:.4f}")

print(f'''
Model Performance:

By predicting the whole year\'s rainfall based purely on the region and the January-May rainfall, the Linear Regression model achieves the following metrics:

 Root Mean Squared Error (RMSE): {rmse:.2f} mm (On average, the model's prediction is off by about {round(rmse, 0)} mm of rainfall).
 R-Squared : {r2:.4f} (The model can explain roughly {round(r2*100, 0)} of the variance in annual rainfall before the heavy monsoon months even happen, largely because geography is a massive driver of expected weather!)

''')

# Serialize and Save Model pipeline using Joblib
joblib.dump(model, "rainfall_model_pipeline.joblib")

print("Model pipeline successfully exported to disk as .joblib files!")