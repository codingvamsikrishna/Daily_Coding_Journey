import pandas as pd

df = pd.read_csv("sample_data.csv")

it_employees = df[df["Department"] == "IT"]

print(it_employees)
