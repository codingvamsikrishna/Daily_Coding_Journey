import pandas as pd

df = pd.read_csv("employees.csv")

average_salary = df["Salary"].mean()

df["Salary"] = df["Salary"].fillna(average_salary)

print(df)
