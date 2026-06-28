import pandas as pd

df = pd.read_csv("sample_data.csv")

result = df[df["Salary"].between(45000, 60000)]

print(result)
