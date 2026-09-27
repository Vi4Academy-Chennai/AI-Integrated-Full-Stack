# train_regression.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Create a sample dataset (e.g., House Size & Rooms vs Price)
data = {
    "feature1": [1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000], # Square Footage
    "feature2": [2, 3, 3, 4, 4, 5, 5, 5],                       # Number of Rooms
    "target_price": [180000, 220000, 260000, 290000, 310000, 350000, 390000, 420000] # Price ($)
}

df = pd.DataFrame(data)

# Separate features (X) and target (y)
X = df[["feature1", "feature2"]]
y = df["target_price"]

# 2. Split dataset into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Extract Intercept and Coefficients
print("=== Model Parameters ===")
print(f"Intercept (Beta 0): {model.intercept_:.2f}")
print(f"Coefficients (Beta 1, Beta 2): {model.coef_}\n")

# 5. Make predictions on the test set
y_pred = model.predict(X_test)

# 6. Evaluate Performance Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== Evaluation Metrics ===")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"Mean Squared Error (MSE): {mse:,.2f}")
print(f"R² Score: {r2:.4f}")