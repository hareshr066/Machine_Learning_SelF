#Step 1: Prepare the dataset !!!!!
import pandas as pd
import numpy as np

data = {
    "Age": [25, 30, 35, np.nan, 40, 45],
    "Salary": [30000, 50000, 60000, 45000, 80000, 90000],
    "City": ["Chennai", "Delhi", "Chennai", "Mumbai", "Delhi", "Mumbai"],
    "Purchased": [0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

#Step 2: Split training and testing data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

#Step 3: Create preprocessing pipelines !!
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Numerical features
num_features = ["Age", "Salary"]

# Categorical features
cat_features = ["City"]

# Numerical preprocessing
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Categorical preprocessing
cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both pipelines
preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_features),
    ("cat", cat_pipeline, cat_features)
])

# Fit on training data and transform it
X_train_processed = preprocessor.fit_transform(X_train)

# Only transform test data
X_test_processed = preprocessor.transform(X_test)

print(X_train_processed)