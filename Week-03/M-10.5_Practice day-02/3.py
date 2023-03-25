class Employee:
    def __init__(self,name,salary,email):
        self.name = name
        self.salary = salary
        self.email = email

employee = Employee('Jafrul',10000,'jafrul22@gmail.com')
print(vars(employee))