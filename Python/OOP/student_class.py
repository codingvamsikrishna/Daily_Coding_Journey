# Student Class Program

class Student:

    def __init__(self, name, course):

        self.name = name
        self.course = course

    def display(self):

        print("Name:", self.name)
        print("Course:", self.course)


student = Student("Vamsi", "MCA")

student.display()
