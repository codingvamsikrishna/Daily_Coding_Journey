import pandas as pd

df = pd.read_csv("employees.csv")

print("Average Salary:", df["Salary"].mean())

print("Maximum Salary:", df["Salary"].max())

print("Minimum Salary:", df["Salary"].min())
