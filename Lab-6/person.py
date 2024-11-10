#  Write a program to create a class called "Person" with a name and age attribute. 
#Create two instances of the "Person" class, 
#set their attributes using the constructor, and print their name and age. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating two instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Printing name and age of each person
print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)

print("\nPerson 2:")
print("Name:", person2.name)
print("Age:", person2.age)


