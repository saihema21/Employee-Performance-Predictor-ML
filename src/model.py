import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# LOAD DATA
data = pd.read_csv("data/employee_data.csv")

# ENCODE CATEGORICAL VARIABLES
le_department = LabelEncoder()
le_job = LabelEncoder()
le_target = LabelEncoder()

data['department'] = le_department.fit_transform(data['department'])
data['job_level'] = le_job.fit_transform(data['job_level'])
data['performance'] = le_target.fit_transform(data['performance'])

# SPLIT DATA
X = data.drop('performance', axis=1)
y = data['performance']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TRAIN MODEL
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# PREDICTION
y_pred = model.predict(X_test)

# EVALUATION
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# SAVE MODEL
joblib.dump(model, "models/performance_model.pkl")

print("\nModel saved successfully!")