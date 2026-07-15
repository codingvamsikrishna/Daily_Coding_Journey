import pandas as pd

df = pd.read_csv("employees.csv")

median_salary = df["Salary"].median()

df["Salary"] = df["Salary"].fillna(median_salary)

print(df)



