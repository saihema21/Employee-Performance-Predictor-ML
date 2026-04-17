import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

# Categories
departments = ['IT', 'HR', 'Sales']
job_levels = ['Junior', 'Mid', 'Senior']

# Generate data
data = pd.DataFrame({
    'age': np.random.randint(22, 60, n),
    'experience': np.random.randint(1, 20, n),
    'department': np.random.choice(departments, n),
    'job_level': np.random.choice(job_levels, n),
    'salary': np.random.randint(20000, 100000, n),
    'training_hours': np.random.randint(0, 50, n),
    'projects_completed': np.random.randint(1, 20, n),
    'attendance_rate': np.random.uniform(0.5, 1.0, n),
    'feedback_score': np.random.uniform(1, 5, n)
})

# Create realistic performance logic
def assign_performance(row):
    score = (
        row['projects_completed'] * 0.3 +
        row['attendance_rate'] * 10 +
        row['feedback_score'] * 2 +
        row['training_hours'] * 0.1
    )

    if score > 20:
        return 'High'
    elif score > 15:
        return 'Medium'
    else:
        return 'Low'

data['performance'] = data.apply(assign_performance, axis=1)

# Save dataset
data.to_csv("data/employee_data.csv", index=False)

print("Dataset created successfully!")
print(data.head())