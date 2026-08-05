# Polymorphism in Python

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Calling the same method
a.sound()
d.sound()
c.sound()