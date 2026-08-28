# Loan Approval EDA + Feature Engineering

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) and Feature Engineering on a Loan Approval dataset.

The main objective is to analyze applicant financial information and understand the factors associated with loan approval.

---

## 2. Problem Statement

Analyze financial information to understand factors associated with loan approval.

---

## 3. Dataset

**Dataset:** `10_loan_approval.csv`

The dataset contains the following columns:

- `age`
- `income_lakh`
- `credit_score`
- `loan_amount_lakh`
- `existing_loans`
- `approved`

Here, `approved` is the target variable.

---

## 4. Objectives

The main objectives of this project are:

- Inspect the dataset structure and statistics.
- Understand the shape, columns, and data types.
- Identify missing values.
- Identify duplicate rows.
- Detect unrealistic and invalid values.
- Analyze the distribution of loan approvals.
- Study credit score, income, and loan amount in relation to approval.
- Identify numerical relationships using correlation analysis.
- Clean the dataset.
- Create meaningful features.
- Re-check the cleaned dataset.
- Separate features (`X`) and target (`y`).

---

## 5. Exploratory Data Analysis

The dataset was loaded using Pandas and inspected using basic EDA techniques.

The following checks were performed:

### Dataset Inspection

- Number of rows and columns
- Column names
- Data types
- Descriptive statistics

### Data Quality Checks

The following were investigated:

- Missing values
- Duplicate rows
- Unrealistic ages
- Invalid credit scores
- Negative income values
- Negative existing loan values

---

## 6. Data Visualization

The project uses Matplotlib and Seaborn to understand the data visually.

The following visualizations were created:

- Approved vs Rejected loan applications
- Credit score distribution
- Income distribution
- Credit score vs approval
- Income vs approval
- Loan amount vs approval
- Boxplots for numerical features and outlier analysis
- Correlation heatmap

These visualizations help identify patterns, distributions, outliers, and relationships between financial features and loan approval.

---

## 7. Data Cleaning

The dataset was cleaned by handling common data-quality issues.

The cleaning process included:

- Removing duplicate rows
- Identifying invalid values
- Handling unrealistic ages
- Handling invalid credit scores
- Handling negative income values
- Handling negative existing loan values
- Handling missing numerical values

Median values were used where appropriate for numerical missing-value treatment.

The cleaned dataset was saved as:

`loan_approval_cleaned.csv`

---

## 8. Feature Engineering

Two additional features were created during the feature-engineering stage.

### 8.1 Debt Burden

A feature named `debt_burden` was created to represent the applicant's existing financial burden relative to their income.

This provides an additional measure of the applicant's financial position.

### 8.2 High Credit Score

A feature named `high_credit_score` was created to identify applicants with a high credit score.

This provides an additional indicator of creditworthiness.

---

## 9. Re-checking the Cleaned Dataset

After cleaning and feature engineering, the dataset was re-checked to ensure that:

- Data-quality issues were addressed.
- The new features were successfully created.
- The dataset was ready for further analysis.

The final cleaned dataset was saved as:

`loan_approval_cleaned.csv`

---

## 10. Feature and Target Separation

The dataset was divided into input features and the target variable.

### Features (X)

`X` contains the independent variables used to analyze loan approval.

### Target (y)

`y` contains:

`approved`

The `approved` column is the target variable for the project.

---

## 11. Technologies Used

The project was completed using basic Python data-analysis tools:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 12. Project Files

```text
Loan-Approval-EDA/
│
├── .gitattributes
├── 10_loan_approval.csv
├── loan_approval_eda.py
├── loan_approval_cleaned.csv
└── README.md