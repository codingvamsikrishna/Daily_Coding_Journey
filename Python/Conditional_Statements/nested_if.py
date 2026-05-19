# Nested If Example

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("License required")
else:
    print("Under age")
