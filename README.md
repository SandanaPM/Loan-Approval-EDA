# Loan Approval EDA + Feature Engineering

## Project Overview

This project analyzes financial information to understand the factors associated with loan approval using Exploratory Data Analysis (EDA) and Feature Engineering.

## Problem Statement

Analyze financial information to understand factors associated with loan approval.

## Dataset

The dataset contains the following features:

- `age`
- `income_lakh`
- `credit_score`
- `loan_amount_lakh`
- `existing_loans`
- `approved` — Target variable

## Objectives

- Inspect the dataset structure and statistics
- Identify missing values and duplicate rows
- Detect unrealistic and invalid values
- Analyze loan approval patterns
- Visualize important features
- Create a correlation heatmap
- Clean the dataset
- Perform feature engineering
- Separate features (X) and target (y)

## Exploratory Data Analysis

The following analyses were performed:

- Dataset shape and information
- Descriptive statistics
- Missing-value analysis
- Duplicate-value analysis
- Invalid-value detection
- Approved vs Rejected visualization
- Credit-score distribution
- Income distribution
- Credit Score vs Approval
- Income vs Approval
- Loan Amount vs Approval
- Correlation heatmap

## Data Cleaning

The dataset was cleaned by handling:

- Missing values
- Duplicate records
- Unrealistic ages
- Invalid credit scores
- Negative income
- Negative existing loans

The cleaned dataset is saved as:

`loan_approval_cleaned.csv`

## Feature Engineering

A new feature called `debt_burden` was created to represent the applicant's financial burden relative to income.

An additional useful feature was also created during the feature-engineering process.

## Target Variable

The target variable is:

`approved`

The dataset was separated into:

- **X** — Input features
- **y** — Target variable (`approved`)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
Loan-Approval-EDA/
│
├── 10_loan_approval.csv
├── loan_approval_eda.py
├── loan_approval_cleaned.csv
└── README.md