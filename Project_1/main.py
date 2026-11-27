import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# we are using this remotive api for this project (https://remotive.com/api/remote-jobs)
url = "https://remotive.com/api/remote-jobs"

# sending request :
response =requests.get(url,params={"limit":10},timeout=20)
#check the response :
print("Status:" ,response.status_code)
# raising the exception if not succeed :
response.raise_for_status()
#converting the data to dict:
data = response.json()

print(type(data))
print(data.keys())

#extract jobs :
jobs=data["jobs"]
print("Number of the jobs here:",len(jobs))
print(jobs[0])

df = pd.DataFrame(jobs)
print(df.head())
print("shape of the dataset is :",df.shape)
print(df.columns)

print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
print(df.describe())

print("\nDuplicate records:")
print(df["id"].duplicated().sum())
# Select relevant columns
df = df[
    [
        "id", "title", "company_name",
        "category", "tags", "job_type",
        "publication_date",
        "candidate_required_location",
        "salary", "url", "description"
    ]
].copy()

# Check duplicate job IDs
df = df.drop_duplicates(subset="id")

# Check missing values
print(df.isnull().sum())

# Remove unnecessary HTML from descriptions
from bs4 import BeautifulSoup

df["description"] = df["description"].apply(
    lambda x: BeautifulSoup(x, "html.parser").get_text(" ", strip=True)
)

print("Cleaned shape:", df.shape)

#Now the interesting part: AI/ML job analysis  (important part)
# in this we are looking for the keywords
# | = or , & = and , used for checking !
# Search across title, category, tags, and description
search_columns = ["title", "category", "description"]

pattern = (
    r"machine learning|artificial intelligence|"
    r"data scientist|data science|AI engineer|"
    r"ML engineer|deep learning|LLM|generative AI"
)

mask = (
    df[search_columns]
    .fillna("")
    .agg(" ".join, axis=1)
    .str.contains(pattern, case=False, na=False)
)

ai_jobs = df[mask].copy()

print("AI/ML jobs:", len(ai_jobs))
print(ai_jobs[["title", "company_name", "category"]].to_string(index=False))

from collections import Counter

# Flatten all job tags into one list
all_tags = [
    tag.lower()
    for tags in ai_jobs["tags"]
    for tag in tags
]

# Count how often each skill appears
skill_counts = Counter(all_tags)

# Convert to a Pandas Series and show top 10
skills = pd.Series(skill_counts).sort_values(ascending=False)
print(skills.head(10))

# ================ Visualizations ====================

top_skills = skills.head(10).sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_skills.values,
    y=top_skills.index
)
plt.title("Top 10 Skills in AI/ML Job Listings")
plt.xlabel("Number of Mentions")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()

#Analyze job types :
print(ai_jobs["job_type"].value_counts())
sns.countplot(
    data=ai_jobs,
    y="job_type",
    order=ai_jobs["job_type"].value_counts().index
)
plt.title("AI/ML Jobs by Employment Type")
plt.xlabel("Number of Jobs")
plt.ylabel("Job Type")
plt.tight_layout()
plt.show()