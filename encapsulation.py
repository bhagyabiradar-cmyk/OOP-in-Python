class Student:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Creating object
s = Student("Alice", 20)

# Accessing public attribute
print("Name:", s.name)

# Accessing private attribute using getter
print("Age:", s.get_age())

# Modifying private attribute using setter
s.set_age(25)
print("Updated Age:", s.get_age())