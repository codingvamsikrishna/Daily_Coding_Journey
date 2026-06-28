import pandas as pd

df = pd.read_csv("sample_data.csv")

result = df.query("Salary > 50000")

print(result)
