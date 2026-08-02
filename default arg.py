class Employee:
    def __init__(self, name="Unknown", salary=0):
        self.name = name
        self.salary = salary

e1 = Employee()
e2 = Employee("John", 50000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)