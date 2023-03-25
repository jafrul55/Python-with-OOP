#Laptop,phone,watch,tablet
#inheritance:
#DRY --> Do not Repeat Yourself
#Base class will have only the common attributes and methods:
#class and def method -> common and uncommon
class Laptop:
    def __init__(self,brand,price,color,dics_size):
        self.brand = brand
        self.price = price
        self.color = color
        self.dics_size = dics_size

    def run(self):
        print('running the laptop')

    def purchase(self,money):
        if money < self.price:
            return 'No laptop for you'
        else:
            print('This device is for you')
            return money - self.price
        
class Phone:
    def __init__(self,brand,price,color,camera,sim_number):
                 self.brand = brand
                 self.price = price
                 self.color = color
                 self.camera = camera
                 self.sim_number = sim_number
    #user define function:
    def is_dual_sim(self):
         return self.sim_number > 1

class Watch:
     def __init_(self,brand,price,color,watch_type):
          self.brand = brand
          self.price = price
          self.color = color
          self.watch_type = watch_type

     def is_digital(self):
          return self.watch_type == 'digital'
     
class Manager:
     def __init__(self,name,salary,experiance,designation):
          pass
     
     def withdraw_salary(self):
          pass
     
     def day_total_sales(self):
          pass
     
     def handle_customer_complain(self):
          pass
     
class SalesPerson:
     def __init__(self,name,salary,experience,designation,commission):
          pass
     
     def withdraw_salary(self):
          pass
     
     def handle_customer(self):
          pass

    
