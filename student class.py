class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)

s1 = Student("Bhagya", 21, 95)
s1.display()