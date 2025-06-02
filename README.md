# Titanic Exploratory Data Analysis

This project is part of a Data Analyst Internship task focused on performing exploratory data analysis (EDA) using the Titanic dataset.

## 📋 Objective
To explore the Titanic dataset visually and statistically to uncover patterns, trends, and insights related to passenger survival.

## 📁 Files
- `Titanic_EDA_Task5.ipynb`: Jupyter Notebook containing the full EDA process.
- `train.csv`: Titanic dataset used for analysis.
- `README.md`: Description of the project and findings.

## 🧰 Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

## 🔍 Key Insights
- Females had a much higher survival rate than males.
- First-class passengers had the highest survival rate.
- Higher ticket fares were associated with better survival chances.
- Age, class, and fare showed significant influence on survival.
- Some columns contain missing values (Age, Cabin).

## 📌 How to Run
1. Make sure you have Python installed.
2. Install required libraries with:
   ```
   pip install pandas seaborn matplotlib
   ```
3. Open the notebook in Jupyter and run all cells.

---

_This analysis helps demonstrate the importance of EDA in understanding data before building any machine learning models._
---

## ❓ Internship EDA Questions & Answers

### 1. What is EDA and why is it important?
**EDA (Exploratory Data Analysis)** is the process of visually and statistically analyzing data before modeling. It helps identify patterns, trends, missing values, and outliers.

**Example:** In the Titanic dataset, EDA shows that females and first-class passengers had higher survival rates.

---

### 2. Which plots do you use to check correlation?
- **Heatmap**: Color-coded correlation matrix.
- **Pairplot**: Scatterplot matrix showing relationships between multiple variables.

**Example:** A heatmap may show that Fare and Pclass are negatively correlated.

---

### 3. How do you handle skewed data?
- Apply transformations like **log()**
- Use **median** instead of mean
- Remove or cap outliers

**Example:** Fare in the Titanic dataset is skewed. `np.log(df['Fare'])` can reduce the skew.

---

### 4. How to detect multicollinearity?
- Use **correlation heatmaps**
- Calculate **VIF (Variance Inflation Factor)**

**Example:** If Pclass and Fare are highly correlated, you might drop one in modeling.

---

### 5. What are univariate, bivariate, and multivariate analyses?

| Type         | Description                      | Example                                 |
|--------------|----------------------------------|-----------------------------------------|
| Univariate   | One variable                     | Histogram of Age                        |
| Bivariate    | Two variables                    | Boxplot of Age vs. Survived             |
| Multivariate | Three or more variables          | Pairplot of Age, Fare, and Survived     |

---

### 6. Difference between heatmap and pairplot?

| Heatmap                          | Pairplot                          |
|----------------------------------|-----------------------------------|
| Shows numeric **correlations**   | Shows **relationships visually**  |
| Works with numeric values        | Works with numeric + categorical  |
| Color-based                      | Scatterplot matrix                |

---

### 7. How do you summarize your insights?
List the most important patterns discovered during EDA, such as survival by gender/class, missing data, and any correlations.

**Example:** "Females had higher survival. 1st-class passengers had better chances. Fare is positively related to survival."

---
