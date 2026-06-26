import pandas as pd

df = pd.read_csv("employees.csv")

high_salary = df[df["Salary"] > 50000]

high_salary.to_csv("high_salary.csv", index=False)

print(high_salary)
