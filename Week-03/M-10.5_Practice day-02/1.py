class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

print(type(Employee))

print(vars(Employee))
print(Employee.__module__)
