import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# 1. Create new features
df["Total"] = df["Maths"] + df["Science"]

df["Average"] = df["Total"] / 2

# 2. Extract date features
df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek

# 3. One-Hot Encoding
df = pd.get_dummies(
    df,
    columns=["City"],
    dtype=int
)

# 4. Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder(
    categories=[["Low", "Medium", "High"]]
)

df["Level"] = encoder.fit_transform(
    df[["Level"]]
)

# 5. Log Transformation
df["Log_Salary"] = np.log1p(df["Salary"])

print(df.head())