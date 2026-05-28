# Custom Exception Example

age = int(input("Enter age: "))

if age < 18:
    raise Exception("Age must be 18 or above")

print("Eligible")
