# Multiple Exceptions Example

try:
    a = 10
    b = int(input("Enter number: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
