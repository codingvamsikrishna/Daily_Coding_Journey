import pandas as pd

df = pd.read_csv("employees.csv")

df["Department"] = df["Department"].fillna("Unknown")

print(df)
