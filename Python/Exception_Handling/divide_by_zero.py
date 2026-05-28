# Divide By Zero Program

try:
    number = int(input("Enter number: "))

    result = 100 / number

    print(result)

except ZeroDivisionError:
    print("Zero division is not allowed")
