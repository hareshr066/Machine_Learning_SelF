import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Arun", "Bala", "Charan", "David"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 75, 95]
}

df = pd.DataFrame(data)
sns.histplot(data=df, x="Marks", kde=True)

plt.title("Distribution of Student Marks")
plt.show()
sns.heatmap(
    df[["Age", "Marks"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.show()