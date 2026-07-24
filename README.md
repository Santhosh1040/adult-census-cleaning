# Adult Census Income Dataset - Data Cleaning Pipeline

## Overview

This project implements a modular data cleaning pipeline for the Adult Census Income dataset using Python and Pandas. The pipeline preprocesses the raw dataset by handling missing values, standardizing categorical data, removing duplicate records, validating the cleaned dataset, and performing exploratory data analysis (EDA).

---

## Project Structure

```text
adult-census-cleaning/
│
├── data/
│   ├── raw/
│   │   └── adult.csv
│   └── processed/
│       └── adult_cleaned.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── reports/
│   └── figures/
│       ├── income_distribution.png
│       ├── age_distribution.png
│       ├── education_distribution.png
│       ├── occupation_distribution.png
│       └── correlation_heatmap.png
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
├── summary_report.md
├── requirements.txt
└── .gitignore
```

---

## Features

- Load and inspect the raw dataset
- Profile the dataset before cleaning
- Replace `'?'` placeholders with missing values (`NaN`)
- Standardize categorical values by removing extra whitespace
- Handle missing values using mode imputation
- Remove duplicate records
- Validate the cleaned dataset
- Save the cleaned dataset
- Generate exploratory data analysis (EDA) visualizations

---

## Data Cleaning Workflow

```text
Load Dataset
      ↓
Profile Raw Dataset
      ↓
Replace '?' with NaN
      ↓
Standardize Categorical Values
      ↓
Handle Missing Values
      ↓
Remove Duplicate Records
      ↓
Validate Dataset
      ↓
Save Cleaned Dataset
      ↓
Perform Exploratory Data Analysis
```

---

## Exploratory Data Analysis

The project generates the following visualizations:

- Income Distribution
- Age Distribution
- Education Distribution
- Occupation Distribution
- Correlation Heatmap

The generated figures are saved in the `reports/figures/` directory.

---

## Technologies Used

- Python 3
- Pandas
- Matplotlib

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd adult-census-cleaning
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the pipeline using:

```bash
python main.py
```

---

## Output

After execution, the project generates:

- Cleaned dataset (`data/processed/adult_cleaned.csv`)
- Validation report
- EDA figures in `reports/figures/`

---

## Dataset

**Adult Census Income Dataset**

The dataset contains demographic and employment-related information used for predicting whether an individual's annual income exceeds \$50K.

---

