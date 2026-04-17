import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# LOAD MODEL
model = joblib.load("models/performance_model.pkl")

# CREATE SAMPLE NEW EMPLOYEE DATA
new_employee = pd.DataFrame({
    'age': [30],
    'experience': [5],
    'department': ['IT'],
    'job_level': ['Mid'],
    'salary': [50000],
    'training_hours': [20],
    'projects_completed': [10],
    'attendance_rate': [0.9],
    'feedback_score': [4]
})

# ENCODING (same as training)
le_department = LabelEncoder()
le_job = LabelEncoder()

le_department.fit(['IT', 'HR', 'Sales'])
le_job.fit(['Junior', 'Mid', 'Senior'])

new_employee['department'] = le_department.transform(new_employee['department'])
new_employee['job_level'] = le_job.transform(new_employee['job_level'])

# PREDICT
prediction = model.predict(new_employee)

# MAP OUTPUT
labels = ['High', 'Low', 'Medium']
result = labels[prediction[0]]

print("Predicted Employee Performance:", result)