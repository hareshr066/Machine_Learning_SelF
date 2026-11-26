import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Charan", "David"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 75, 95]
}

df = pd.DataFrame(data)

print(df)
print(df.head())             # First five rows
print(df.tail())             # Last five rows
print(df.shape)              # Rows and columns
print(df.info())             # Column information
print(df.describe())         # Statistical summary
print(df["Marks"].mean())    # Average marks

# Filtering
print(df[df["Marks"] > 80])

# Sorting
print(df.sort_values("Marks", ascending=False))
df.isnull().sum()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())