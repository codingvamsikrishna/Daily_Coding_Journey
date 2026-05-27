# Student Record Program

file = open("students.txt", "w")

name = input("Enter student name: ")
course = input("Enter course: ")

file.write("Name: " + name + "\n")
file.write("Course: " + course)

file.close()

print("Student record saved")
