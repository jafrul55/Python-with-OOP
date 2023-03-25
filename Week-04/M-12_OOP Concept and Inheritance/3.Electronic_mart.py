#inheritance:
#Base class will have only the common attributes and methods:
class Device:
     def __init__(self,brand,price,color):
          self.brand = brand
          self.price = price
          self.color = color
     
     def re_sell(self):
          print("Ready to sell again")

#laptop inherit to Device
class Laptop(Device):
     def __init__(self,brand,price,color,dics_size):
        
     #you can get brand,price,color for inheritance:
        super().__init__(brand,price,color)

        self.dics_size = dics_size

     def run(self):
        print('running the laptop')
     #Representation Method:
     def __repr__(self) -> str:
          return f'Laptop {self.brand} : {self.price} : {self.color}'

     def purchase(self,money,discount):
        if money < (self.price - self.price * discount/100):
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
    
     def purchase(self,money,discount):
          if money < (self.price - self.price * discount/100):
               return 'No Phone for you'
          else:
               print('This device is for you')
               return money - self.price
          
     def __repr__(self) -> str:
          return f'Phone {self.brand} : {self.price} : {self.color}'

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

lenovo = Laptop('Lenovo',4200,'black','500gb')
hp = Laptop('HP',35000,'silver','250gb')

print(lenovo)
print(hp)
#inherit:
hp.re_sell()
print(hp.brand)

oppo = Phone('OPPO',15000,'black','15MP',2)
samsung = Phone('SAMSUNG',21000,'silver','12mp',1)

print(oppo)
print(samsung)


    
