# train_classification.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# 1. Create a sample classification dataset (Monthly Charges & Tenure vs Churn)
# Target: churn (0 = Retained, 1 = Churned)
data = {
    "monthly_charges": [30.5, 85.0, 92.5, 20.0, 95.0, 45.0, 88.0, 22.5, 90.0, 78.0],
    "tenure_months": [24, 3, 2, 36, 1, 18, 4, 30, 2, 5],
    "churn": [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Separate features (X) and target labels (y)
X = df[["monthly_charges", "tenure_months"]]
y = df["churn"]

# 2. Split dataset into Training (70%) and Testing (30%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Initialize and train the Logistic Regression classifier
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Make predictions on the test set
y_pred = model.predict(X_test)

# 5. Generate Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("=== Confusion Matrix ===")
print(conf_matrix)
print("\n[ Format: ]")
print("[ True Negatives (TN)  False Positives (FP) ]")
print("[ False Negatives (FN)  True Positives (TP)  ]\n")

# 6. Generate Detailed Classification Report
print("=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=["Retained (0)", "Churned (1)"]))

# 7. Calculate Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Overall Accuracy: {acc * 100:.2f}%")