# Inheritance Example

class Person:

    def speak(self):
        print("Person can speak")


class Student(Person):
    pass


s = Student()

s.speak()
