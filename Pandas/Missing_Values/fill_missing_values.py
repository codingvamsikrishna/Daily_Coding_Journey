import pandas as pd

df = pd.read_csv("employees.csv")

new_df = df.fillna("Not Available")

print(new_df)
