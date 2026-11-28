import pandas as pd

df = pd.read_csv("data.csv")

# Correlation matrix
corr = df.corr(numeric_only=True)

print(corr)

# Correlation with target
print(corr["Salary"].sort_values(ascending=False))

# selectkbest
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

selector = SelectKBest(
    score_func=f_classif,
    k=3
)

X_train_selected = selector.fit_transform(X_train, y_train)

X_test_selected = selector.transform(X_test)

print("Selected Features:", X.columns[selector.get_support()])

