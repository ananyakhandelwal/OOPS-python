# Create a class named 'Student' with String variable 'name' and integer variable 'roll_no'.
#Assign the value of roll no as '2' and that of name as "John" by creating an object of the class Student. 

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# Creating an instance of the Student class with name "John" and roll_no 2
student = Student("John", 2)

# Printing the name and roll number of the student
print("Student Name:", student.name)
print("Student Roll Number:", student.roll_no)

