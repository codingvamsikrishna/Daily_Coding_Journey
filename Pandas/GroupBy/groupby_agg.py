import pandas as pd

df = pd.read_csv("employees.csv")

result = df.groupby("Department").agg({
    "Salary": ["sum", "mean", "max", "min"],
    "Experience": "mean"
})

print(result)

