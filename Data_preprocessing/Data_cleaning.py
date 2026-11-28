
import pandas as pd
import numpy as np

# ==========================================
# 1. CREATE / LOAD DATA
# ==========================================

# In real projects, use:
# df = pd.read_csv("data.csv")

data = {
    "Name": ["John", "Alex", "Sam", "John", "Mike", None],
    "Age": [25, 30, np.nan, 25, 150, 28],
    "Salary": [50000, 60000, 45000, 50000, 70000, np.nan],
    "City": ["Chennai", "Delhi", "chennai", "Chennai", "Mumbai", None],
    "Experience": [2, 5, 3, 2, 10, 4]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ==========================================
# 2. UNDERSTANDING THE DATA
# ==========================================

print("\n--- Dataset Information ---")

print(df.head())             # First 5 rows
print(df.tail())             # Last 5 rows
print(df.shape)              # Rows and columns
print(df.columns)            # Column names
print(df.info())              # Data types and null counts
print(df.describe())          # Numerical statistics
print(df.dtypes)              # Column data types


# ==========================================
# 3. HANDLING MISSING VALUES
# ==========================================

# Count missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Percentage of missing values
print("\nMissing Percentage:")
print(df.isnull().mean() * 100)

# Remove rows containing missing values
# df.dropna(inplace=True)

# Remove columns containing missing values
# df.dropna(axis=1, inplace=True)

# Fill numerical columns with median
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

# Fill categorical columns with mode
df["Name"] = df["Name"].fillna(
    df["Name"].mode()[0]
)

df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)

print("\nAfter Missing Value Handling:")
print(df.isnull().sum())


# ==========================================
# 4. HANDLING DUPLICATES
# ==========================================

# Count duplicate rows
print("\nDuplicate Count:")
print(df.duplicated().sum())

# Display duplicate rows
print(df[df.duplicated()])

# Remove duplicate rows
df.drop_duplicates(inplace=True)


# ==========================================
# 5. HANDLING INCORRECT DATA TYPES
# ==========================================

# Convert column to numeric
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

# Convert column to string
df["City"] = df["City"].astype("string")

# Convert dates to datetime
# df["Date"] = pd.to_datetime(df["Date"])


# ==========================================
# 6. HANDLING INCONSISTENT CATEGORICAL DATA
# ==========================================

# Remove unnecessary spaces
df["City"] = df["City"].str.strip()

# Convert text into consistent lowercase
df["City"] = df["City"].str.lower()

print("\nUnique Cities:")
print(df["City"].unique())


# ==========================================
# 7. DETECTING OUTLIERS USING IQR
# ==========================================

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identify potential outliers
outliers = df[
    (df["Age"] < lower) |
    (df["Age"] > upper)
]

print("\nPotential Outliers:")
print(outliers)

# Optional: Remove outliers
# Only do this when domain knowledge justifies it.
# df = df[(df["Age"] >= lower) & (df["Age"] <= upper)]


# ==========================================
# 8. HANDLING INVALID VALUES
# ==========================================

# Example: Age should not be negative
df.loc[df["Age"] < 0, "Age"] = np.nan

# Example: Salary should not be negative
df.loc[df["Salary"] < 0, "Salary"] = np.nan


# ==========================================
# 9. FINAL DATA VALIDATION
# ==========================================

print("\n--- Final Dataset ---")

print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDataset Shape:")
print(df.shape)


# ==========================================
# 10. SAVE CLEANED DATA
# ==========================================

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
