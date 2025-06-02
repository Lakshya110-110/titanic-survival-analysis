# 🚢 Titanic EDA – Internship Task 5

This repository contains the solution for **Task 5: Exploratory Data Analysis (EDA)** from the Data Analyst Internship program. The goal is to uncover patterns, trends, and insights from the Titanic dataset using Python-based visualization and statistical techniques.

---

## 📁 Files Included

| File Name                       | Description                                           |
|--------------------------------|-------------------------------------------------------|
| `train.csv`                    | Titanic dataset from Kaggle                          |
| `Titanic_EDA_Task5.ipynb`      | Jupyter Notebook performing full EDA                |
| `Titanic_EDA_Task5_Corrected.ipynb` | Cleaned version compatible with Jupyter/VS Code  |
| `titanic_analysis.py`          | Python script with same EDA analysis as `.ipynb`     |
| `TASK 5 DA.pdf`                | Internship-provided task description                 |
| `README.md`                    | Project overview and documentation                   |

---

## 🧠 Objective

- Explore the Titanic dataset visually and statistically.
- Understand feature distributions and their relationship with survival.
- Use histograms, boxplots, heatmaps, and pairplots to gain insights.
- Provide observations and a summary of key findings.

---

## 🔧 Tools Used

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- VS Code
- Jupyter Notebook

---

## 📊 Key EDA Insights

- 💡 **Gender Impact**: Females had a much higher survival rate than males.
- 🎟 **Class Impact**: Passengers in 1st class were more likely to survive.
- 💰 **Fare Impact**: Higher fares were linked to higher survival rates.
- 🧒 **Age**: Children and younger passengers had better chances of survival.
- 🔍 **Correlations**: Negative correlation between `Pclass` and survival, positive correlation with `Fare`.
- ⚠️ **Missing Data**: Columns like `Cabin` and `Age` have missing values.

---

## 🧪 How to Run

1. Clone the repo or download the files.
2. Install dependencies (if needed):

```bash
pip install pandas matplotlib seaborn notebook
