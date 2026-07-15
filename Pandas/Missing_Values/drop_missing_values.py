import pandas as pd

df = pd.read_csv("employees.csv")

new_df = df.dropna()

print(new_df)

