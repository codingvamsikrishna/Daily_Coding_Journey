import pandas as pd

df = pd.read_csv("sample_data.csv")

result = df[df["Name"].str.startswith("V")]

print(result)
