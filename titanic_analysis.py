# 1. Importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Display settings
sns.set(style='whitegrid')

# 2. Loading the dataset
df = pd.read_csv("train.csv")
print(df.head())

# 3. Basic information
print("Dataset Info:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nValue Counts for Categorical Columns:")
print(df['Sex'].value_counts())
print(df['Pclass'].value_counts())
print(df['Embarked'].value_counts())

# 4. Univariate Analysis

# Age Distribution
sns.histplot(df['Age'].dropna(), kde=True)
plt.title("Age Distribution")
plt.show()

# Fare Distribution
sns.histplot(df['Fare'], kde=True)
plt.title("Fare Distribution")
plt.show()

# Countplot for Survival
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# Countplot for Passenger Class
sns.countplot(x='Pclass', data=df)
plt.title("Passenger Class Count")
plt.show()

# 5. Bivariate Analysis

# Survival Rate by Sex
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

# Survival Rate by Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()

# Boxplot - Age vs. Survived
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs. Survival")
plt.show()

# 6. Multivariate Analysis

# Heatmap for Correlation (only numeric columns)
plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Pairplot
sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass']], hue='Survived')
plt.suptitle("Pairplot of Key Variables", y=1.02)
plt.show()

# 7. Summary of Findings
summary = """
🔎 SUMMARY OF FINDINGS:

1. **Gender Impact**: Females had a much higher survival rate than males.
2. **Passenger Class Impact**: First-class passengers (Pclass = 1) had a higher survival rate compared to those in lower classes.
3. **Age Trends**: Younger passengers tended to survive more often, but survival was not limited to age.
4. **Fare and Survival**: Higher fares were generally associated with higher survival, possibly reflecting better class.
5. **Correlations**:
   - Pclass is negatively correlated with survival (lower class, lower survival).
   - Fare is positively correlated with survival.
6. **Missing Data**:
   - Columns like 'Age' and 'Cabin' have missing values. 'Cabin' especially has a lot of missing entries.

📌 Insights like these are important for building models or making informed decisions based on historical data.
"""

print(summary)






