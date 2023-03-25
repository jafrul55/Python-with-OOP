class Employee:
    def __init__(self,employee,salary,email):
        self.employee_name = employee
        self.salary = salary
        self.email_address = email


employee = Employee('Jafrul',100000,"jafrulalamtusher22@gmail.com")

print('Orginal Values: ')
print(employee.employee_name)
print(employee.salary)
print(employee.email_address)

print('\n')

print("Modify Value: ")
employee.employee_name = 'Tusar'
employee.salary = 200000
employee.email_address = 'jafrul5782@gmail.com'
print(employee.employee_name)
print(employee.salary)
print(employee.email_address)