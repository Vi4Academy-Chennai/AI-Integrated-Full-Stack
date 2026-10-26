import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# Generate synthetic dataset for demonstration
np.random.seed(42)
n_samples = 1000

data = {
    'sqrft': np.random.randint(500, 5000, n_samples),
    'rooms': np.random.randint(1, 6, n_samples),
    'year_built': np.random.randint(1950, 2024, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples)
}

# Mock realistic price calculation logic
price = (
    (data['sqrft'] * 150) + 
    (data['rooms'] * 25000) + 
    ((data['year_built'] - 1900) * 1000) + 
    (data['location_score'] * 35000)
)
# Add some noise for realism
price += np.random.normal(0, 15000, n_samples)

X = pd.DataFrame(data)
y = price

# Train the model
print("Training the RandomForest model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to disk
joblib.dump(model, 'house_price_model.joblib')
print("Model trained and saved as 'house_price_model.joblib'")