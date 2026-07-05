import pandas as pd

df = pd.read_csv("employees.csv")

result = df.groupby("Department")["Salary"].mean()

print(result)

