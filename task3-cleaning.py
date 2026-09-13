import pandas as pd

df = pd.read_csv("C:\\Users\\Welcome\\Downloads\\10,000 records healthcare data.csv")
df.head()
missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum()
})

display(missing)

if missing["Missing Values"].sum() == 0:
    print("Completeness: PASS")
else:
    print("Completeness: FAIL")


duplicate_names = df[df["Name"].duplicated()]

display(duplicate_names)

duplicate_names = df[""].duplicated().sum()

print("Duplicate names:", duplicate_names)

if duplicate_names.sum() == 0:
    print("Duplicates: PASS")
else:
    print("Duplicates: FAIL")

