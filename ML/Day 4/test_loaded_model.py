import pandas as pd
import joblib

# 1. Load the saved pipeline
loaded_pipeline = joblib.load('rainfall_model_pipeline.joblib')

# 2. Example new data (e.g., predicting annual rainfall for Kerala based on early months)
new_data = pd.DataFrame({
    'SUBDIVISION': ['Kerala'],
    'JAN': [28.5],
    'FEB': [14.2],
    'MAR': [33.1],
    'APR': [110.4],
    'MAY': [250.8]
})

# 3. Make the prediction directly
# The pipeline automatically encodes 'Kerala' and scales the numerical values
predicted_annual_rainfall = loaded_pipeline.predict(new_data)

print(f"Predicted Annual Rainfall: {predicted_annual_rainfall[0]:.2f} mm")