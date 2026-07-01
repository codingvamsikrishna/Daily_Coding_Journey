import pandas as pd

df = pd.read_csv("employees.csv")

result = df.groupby("Department")

print(result)
