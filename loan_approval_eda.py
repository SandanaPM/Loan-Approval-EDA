# ============================================================
# PROBLEM 10 - LOAN APPROVAL
# EDA + FEATURE ENGINEERING
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. LOAD THE DATASET
# ============================================================

df = pd.read_csv("10_loan_approval.csv")

print("=" * 60)
print("1. DATASET INSPECTION")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistics:")
print(df.describe())


# ============================================================
# 2. CHECK MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("2. MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# 3. CHECK DUPLICATE ROWS
# ============================================================

print("\n" + "=" * 60)
print("3. DUPLICATE ROWS")
print("=" * 60)

print("Number of duplicate rows:", df.duplicated().sum())


# ============================================================
# 4. INVESTIGATE INVALID VALUES
# ============================================================

print("\n" + "=" * 60)
print("4. INVALID VALUES")
print("=" * 60)

# Invalid ages
invalid_age = df[(df["age"] < 18) | (df["age"] > 100)]

print("\nInvalid ages:")
print(invalid_age)
print("Number of invalid ages:", len(invalid_age))


# Invalid credit scores
invalid_credit = df[
    (df["credit_score"] < 300) |
    (df["credit_score"] > 850)
]

print("\nInvalid credit scores:")
print(invalid_credit)
print("Number of invalid credit scores:", len(invalid_credit))


# Negative income
invalid_income = df[df["income_lakh"] < 0]

print("\nNegative income:")
print(invalid_income)
print("Number of negative income values:", len(invalid_income))


# Negative existing loans
invalid_loans = df[df["existing_loans"] < 0]

print("\nNegative existing loans:")
print(invalid_loans)
print("Number of negative existing loans:", len(invalid_loans))


# ============================================================
# 5. APPROVED VS REJECTED
# ============================================================

print("\n" + "=" * 60)
print("5. APPROVED VS REJECTED")
print("=" * 60)

print(df["approved"].value_counts())

plt.figure(figsize=(6, 4))
sns.countplot(x="approved", data=df)

plt.title("Loan Approval Status")
plt.xlabel("Approved (0 = Rejected, 1 = Approved)")
plt.ylabel("Number of Applicants")
plt.show()


# ============================================================
# 6. CREDIT SCORE DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 4))

sns.histplot(
    df["credit_score"],
    bins=30,
    kde=True
)

plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.ylabel("Frequency")
plt.show()


# ============================================================
# 7. INCOME DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 4))

sns.histplot(
    df["income_lakh"],
    bins=30,
    kde=True
)

plt.title("Income Distribution")
plt.xlabel("Income (Lakh)")
plt.ylabel("Frequency")
plt.show()


# ============================================================
# 8. CREDIT SCORE VS APPROVAL
# ============================================================

plt.figure(figsize=(7, 4))

sns.boxplot(
    x="approved",
    y="credit_score",
    data=df
)

plt.title("Credit Score vs Loan Approval")
plt.xlabel("Approved (0 = Rejected, 1 = Approved)")
plt.ylabel("Credit Score")
plt.show()

print("\nAverage credit score by approval:")
print(df.groupby("approved")["credit_score"].mean())


# ============================================================
# 9. INCOME VS APPROVAL
# ============================================================

plt.figure(figsize=(7, 4))

sns.boxplot(
    x="approved",
    y="income_lakh",
    data=df
)

plt.title("Income vs Loan Approval")
plt.xlabel("Approved (0 = Rejected, 1 = Approved)")
plt.ylabel("Income (Lakh)")
plt.show()

print("\nAverage income by approval:")
print(df.groupby("approved")["income_lakh"].mean())


# ============================================================
# 10. LOAN AMOUNT VS APPROVAL
# ============================================================

plt.figure(figsize=(7, 4))

sns.boxplot(
    x="approved",
    y="loan_amount_lakh",
    data=df
)

plt.title("Loan Amount vs Loan Approval")
plt.xlabel("Approved (0 = Rejected, 1 = Approved)")
plt.ylabel("Loan Amount (Lakh)")
plt.show()

print("\nAverage loan amount by approval:")
print(df.groupby("approved")["loan_amount_lakh"].mean())


# ============================================================
# 11. CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(8, 6))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()


# ============================================================
# 12. CLEAN THE DATASET
# ============================================================

print("\n" + "=" * 60)
print("12. DATA CLEANING")
print("=" * 60)

# Remove duplicate rows
clean_df = df.drop_duplicates().copy()

# Replace invalid ages with NaN
clean_df.loc[
    (clean_df["age"] < 18) |
    (clean_df["age"] > 100),
    "age"
] = np.nan

# Replace negative income with NaN
clean_df.loc[
    clean_df["income_lakh"] < 0,
    "income_lakh"
] = np.nan

# Replace invalid credit scores with NaN
clean_df.loc[
    (clean_df["credit_score"] < 300) |
    (clean_df["credit_score"] > 850),
    "credit_score"
] = np.nan

# Replace negative existing loans with NaN
clean_df.loc[
    clean_df["existing_loans"] < 0,
    "existing_loans"
] = np.nan


# Fill missing numerical values with median
numeric_columns = [
    "age",
    "income_lakh",
    "credit_score",
    "loan_amount_lakh",
    "existing_loans"
]

for column in numeric_columns:
    clean_df[column] = clean_df[column].fillna(
        clean_df[column].median()
    )

print("Cleaning completed.")


# ============================================================
# 13. CREATE DEBT BURDEN
# ============================================================

print("\n" + "=" * 60)
print("13. FEATURE ENGINEERING - DEBT BURDEN")
print("=" * 60)

clean_df["debt_burden"] = (
    clean_df["loan_amount_lakh"] /
    clean_df["income_lakh"]
)

print(clean_df[
    [
        "income_lakh",
        "loan_amount_lakh",
        "debt_burden"
    ]
].head())


# ============================================================
# 14. CREATE ADDITIONAL FEATURE
# ============================================================

print("\n" + "=" * 60)
print("14. ADDITIONAL FEATURE - HIGH CREDIT SCORE")
print("=" * 60)

clean_df["high_credit_score"] = (
    clean_df["credit_score"] >= 700
).astype(int)

print(clean_df[
    [
        "credit_score",
        "high_credit_score"
    ]
].head())


# ============================================================
# 15. RE-CHECK CLEANED DATASET
# ============================================================

print("\n" + "=" * 60)
print("15. CLEANED DATASET")
print("=" * 60)

print("\nCleaned shape:")
print(clean_df.shape)

print("\nMissing values after cleaning:")
print(clean_df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(clean_df.duplicated().sum())

print("\nCleaned dataset statistics:")
print(clean_df.describe())


# ============================================================
# 16. SEPARATE X AND y
# ============================================================

print("\n" + "=" * 60)
print("16. SEPARATE X AND y")
print("=" * 60)

X = clean_df.drop("approved", axis=1)
y = clean_df["approved"]

print("\nX columns:")
print(X.columns.tolist())

print("\ny column:")
print("approved")

print("\nX shape:", X.shape)
print("y shape:", y.shape)


# ============================================================
# 17. SAVE CLEANED DATASET
# ============================================================

clean_df.to_csv(
    "loan_approval_cleaned.csv",
    index=False
)

print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print("Cleaned dataset saved as:")
print("loan_approval_cleaned.csv")

print("\nEDA + Feature Engineering completed successfully!")