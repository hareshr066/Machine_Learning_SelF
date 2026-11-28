import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler
)

df = pd.read_csv("data.csv")

features = ["Age", "Salary"]

# 1. Standardization
scaler = StandardScaler()

df[features] = scaler.fit_transform(
    df[features]
)

# 2. Min-Max Normalization
scaler = MinMaxScaler()

df[features] = scaler.fit_transform(
    df[features]
)

print(df.head())