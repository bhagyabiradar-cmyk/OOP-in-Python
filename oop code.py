# Parent Class 1
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Parent Class 2
class Walker:
    def walk(self):
        print("Animal can walk")

# Child Class (Multiple Inheritance)
class Dog(Animal, Walker):
    # Polymorphism (Method Overriding)
    def sound(self):
        print("Dog barks")

# Object
d = Dog()

# Calling methods
d.sound()     # Polymorphism
d.walk()      # Inherited from Walker

# Operators
a = 15
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Greater than:", a > b)
print("Equal:", a == b)