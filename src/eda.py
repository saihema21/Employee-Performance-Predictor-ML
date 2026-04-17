import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATA
data = pd.read_csv("data/employee_data.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# -------------------------
# EDA VISUALIZATIONS
# -------------------------

# 1. Performance Distribution
sns.countplot(x='performance', data=data)
plt.title("Employee Performance Distribution")
plt.savefig("outputs/performance_distribution.png")
plt.show()

# 2. Experience vs Performance
sns.boxplot(x='performance', y='experience', data=data)
plt.title("Experience vs Performance")
plt.savefig("outputs/experience_vs_performance.png")
plt.show()

# 3. Training Hours vs Performance
sns.boxplot(x='performance', y='training_hours', data=data)
plt.title("Training Hours vs Performance")
plt.savefig("outputs/training_vs_performance.png")
plt.show()

# 4. Attendance vs Performance
sns.boxplot(x='performance', y='attendance_rate', data=data)
plt.title("Attendance vs Performance")
plt.savefig("outputs/attendance_vs_performance.png")
plt.show()

print("\nEDA Completed!")