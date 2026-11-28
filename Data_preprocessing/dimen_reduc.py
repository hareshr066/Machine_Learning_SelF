import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("data.csv")

# Select numerical features
X = df[["Age", "Salary", "Experience", "Projects"]]

# 1. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

# 3. Check reduced dimensions
print("Original Shape:", X.shape)
print("Reduced Shape:", X_reduced.shape)

# 4. Explained variance
print("Variance:", pca.explained_variance_ratio_)

print("Total Variance:",
      pca.explained_variance_ratio_.sum())