class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")

    def display(self):
        print("Name:", self.name)

    def welcome(self):
        print("Welcome to Python")

s1 = Student("Bhagya")
s1.display()
s1.welcome()