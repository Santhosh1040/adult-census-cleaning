# Adult Census Income Dataset - Data Cleaning Summary Report

## Project Overview

This project focuses on cleaning and preparing the Adult Census Income dataset for further analysis and machine learning tasks. The dataset was processed using a modular Python pipeline that identifies and handles missing values, standardizes categorical data, removes duplicate records, validates the cleaned dataset, and performs exploratory data analysis (EDA).

---

## Dataset Summary

- **Original Dataset Shape:** 32,561 rows × 15 columns
- **Cleaned Dataset Shape:** 32,537 rows × 15 columns
- **Rows Removed:** 24 duplicate records

---

## Data Cleaning Steps

The following preprocessing steps were performed:

1. Loaded the raw dataset using Pandas.
2. Profiled the raw dataset to inspect its structure, data types, and missing value placeholders.
3. Replaced `'?'` placeholders with `NaN` values.
4. Standardized categorical columns by removing leading and trailing whitespace.
5. Filled missing values in the following categorical columns using the mode:
   - `workclass`
   - `occupation`
   - `native.country`
6. Removed duplicate records.
7. Validated the cleaned dataset to ensure:
   - No missing values remain.
   - No duplicate records remain.
8. Saved the cleaned dataset for further use.

---

## Missing Value Handling

The original dataset used `'?'` to represent missing values.

| Column | Missing Values |
|--------|---------------:|
| workclass | 1,836 |
| occupation | 1,843 |
| native.country | 583 |

These values were replaced with `NaN` and then imputed using the most frequent value (mode) for each column.

---

## Validation Results

After preprocessing:

- Missing Values: **0**
- Duplicate Records: **0**
- Final Dataset Shape: **32,537 × 15**

---

## Exploratory Data Analysis

The following visualizations were generated:

- Income Distribution
- Age Distribution
- Education Distribution
- Occupation Distribution
- Correlation Heatmap

All generated figures are available in the `reports/figures/` directory.

---

## Project Structure

```text
adult-census-cleaning/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│   └── figures/
│
├── src/
│   ├── loader.py
│   ├── profiling.py
│   ├── cleaning.py
│   ├── validation.py
│   ├── save_data.py
│   └── eda.py
│
├── main.py
├── README.md
├── requirements.txt
├── summary_report.md
└── .gitignore
```

---

## Conclusion

The Adult Census Income dataset was successfully cleaned and validated using a modular Python pipeline. Missing values were handled, duplicate records were removed, categorical data was standardized, and exploratory data analysis was performed. The cleaned dataset is ready for downstream statistical analysis and machine learning applications.