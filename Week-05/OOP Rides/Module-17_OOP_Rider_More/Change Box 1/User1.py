#Append User info in file and Raise Custom Exception:
import hashlib
from random import random,randint
from unittest import result
from brta1 import BRTA
from Vehicles1 import Car,Bike,Cng
from Ride_Manager1 import uber


#you can also use custom Exception:
class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
            print(f'User: {email} already exists.')
            super().__init__(*args)


license_authority = BRTA()
class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
       #You can also use Boolen:
        already_exists = False
        with open('Users.txt','r') as file:
            if email in file.read():
                already_exists = True
                #use here custom Exception:
                # raise UserAlreadyExists(email)
                # print(f'User: {email} already exists.')
        file.close()
        

        if already_exists == False:
            with open('Users.txt','a') as file:
                file.write(f'{email} {pwd_encrypt}\n')
            file.close()
        print(self.name,'User created')



    @staticmethod
    def log_in(email,password):
        store_password = ''
        with open('Users.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    # print(line)
                    store_password = line.split(' ')[1]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == store_password:
            print('Valid User')
            return True
        else:
            print('Invalid User')
            return False
        # print('Password found: ',store_password)
        
class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self,location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self,destination):
        pass

    def start_a_trip(self,fare):
        self.balance -= fare

class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email,license)
        self.earning = 0
    

    def take_driving_test(self):
        license_authority.take_driving_test(self.email)
        if result == False:
            print("Sorry you failed,try again")
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self,vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            new_vehicle = None
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)            
        else:
            print('You are not a valid driver')


    def start_a_trip(self,destination,fare):
        self.earning += fare
        self.location = destination

rider1 = Rider('rider1','rider1@gmail.com','rider1', randint(0,30),5000)
rider2 = Rider('rider2','rider2@gmail.com','rider2', randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3', randint(0,30),5000)

driver1 = Driver('driver1','driver1@gmail.com','driver1',randint(0,30),5645)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 1245, 10)

driver2 = Driver('driver2','driver2@gmail.com','driver2',randint(0,30),5645)
driver2.take_driving_test()
driver2.register_a_vehicle('car', 2145, 10)

driver3 = Driver('driver3','driver3@gmail.com','driver3',randint(0,30),5645)
driver3.take_driving_test()
driver3.register_a_vehicle('car', 2145, 10)

driver4 = Driver('driver4','driver4@gmail.com','driver4',randint(0,30),5645)
driver4.take_driving_test()
driver4.register_a_vehicle('car', 3245, 10)

print(uber.get_available_cars())

uber.find_a_vehicle(rider1,'car',90)
