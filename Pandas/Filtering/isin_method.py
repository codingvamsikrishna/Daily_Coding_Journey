import pandas as pd

df = pd.read_csv("sample_data.csv")

result = df[df["Department"].isin(["IT", "HR"])]

print(result)

