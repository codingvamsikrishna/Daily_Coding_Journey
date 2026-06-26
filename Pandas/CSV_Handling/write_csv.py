import pandas as pd

data = {
    "Name": ["Amit", "Rahul"],
    "Salary": [40000, 45000]
}

df = pd.DataFrame(data)

df.to_csv("new_employees.csv", index=False)

print("CSV file created successfully.")
