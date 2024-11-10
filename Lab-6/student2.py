# Write a program to define a class Student with attributes like name and age, and create objects to represent different students.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Printing the details of each student
print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)

print("\nStudent 3:")
print("Name:", student3.name)
print("Age:", student3.age)
