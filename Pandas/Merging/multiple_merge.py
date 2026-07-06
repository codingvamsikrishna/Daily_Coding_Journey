import pandas as pd

employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")
locations = pd.read_csv("locations.csv")

result = employees.merge(departments,on="DepartmentID") \
                  .merge(locations,on="DepartmentID")

print(result)
