import pandas as pd

df = pd.read_csv("employees.csv")

print("Total Employees:", len(df))
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
