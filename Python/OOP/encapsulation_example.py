# Encapsulation Example

class Employee:

    def __init__(self):

        self.__salary = 50000

    def show_salary(self):
        print(self.__salary)


emp = Employee()

emp.show_salary()
