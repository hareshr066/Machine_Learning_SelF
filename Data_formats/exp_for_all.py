import pandas as pd

data = {
    "Job": ["ML Engineer", "Data Scientist", "AI Engineer"],
    "Company": ["Google", "Amazon", "Microsoft"],
    "Salary": [120000, 100000, 110000],
    "Remote": [True, False, True],
}

df = pd.DataFrame(data)
print(df)

# Write files
df.to_csv("jobs.csv", index=False)
df.to_excel("jobs.xlsx", index=False)
df.to_json("jobs.json", orient="records", indent=4)
df.to_parquet("jobs.parquet", index=False)

# Read files back into variables
csv_data = pd.read_csv("jobs.csv")
excel_data = pd.read_excel("jobs.xlsx")
json_data = pd.read_json("jobs.json")
parquet_data = pd.read_parquet("jobs.parquet")

datasets = {
    "CSV": csv_data,
    "Excel": excel_data,
    "JSON": json_data,
    "Parquet": parquet_data,
}

for name, dataset in datasets.items():
    print(f"\n{name}")
    print("Shape:", dataset.shape)
    print("Columns:", list(dataset.columns))
    print("Data Types:")
    print(dataset.dtypes)