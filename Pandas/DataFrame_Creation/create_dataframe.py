import pandas as pd

data = {
    "Name": ["Vamsi", "Ram", "Sai"],
    "Age": [23, 24, 22],
    "Department": ["IT", "HR", "Finance"]
}

df = pd.DataFrame(data)

print(df)
