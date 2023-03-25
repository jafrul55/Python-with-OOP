# Implement threading for parallel trips:
import hashlib
from random import random,randint
import threading
from unittest import result
from brta7 import BRTA
from Vehicles7 import Car,Bike,Cng
from Ride_Manager7 import uber


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
        # print(self.name,'User created')


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
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self,location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self,destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self,fare,trip_info):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email,license)
        self.earning = 0
        self.vehicle = None
    

    def take_driving_test(self):
        license_authority.take_driving_test(self.email)
        if result == False:
            # print("Sorry you failed,try again")
            self.license = None
        else:
            self.license = result
            self.valid_driver = True
    
    def register_a_vehicle(self,vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)
            else:
                self.vehicle = Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type, self.vehicle)            
        else:
            print('You are not a valid driver')


    def start_a_trip(self, start, destination,fare,trip_info):
        self.earning += fare
        self.location = destination
        #start thread
        trip_thread = threading.Thread(target=self.vehicle.start_driving,args=(start, destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start, destination)
        self.__trip_history.append(trip_info)

rider1 = Rider('rider1','rider1@gmail.com','rider1', randint(0,30),1000)
rider2 = Rider('rider2','rider2@gmail.com','rider2', randint(0,30),5000)
rider3 = Rider('rider3','rider3@gmail.com','rider3', randint(0,30),5000)
rider4= Rider('rider4','rider4@gmail.com','rider4', randint(0,30),5000)
rider5 = Rider('rider5','rider5@gmail.com','rider5', randint(0,30),5000)

for i in range(1,100):
    driver1 = Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',randint(0,100),randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle('car', randint(10000,99999), 10)

print(uber.get_available_cars())

uber.find_a_vehicle(rider1,'car',randint(1,100))
uber.find_a_vehicle(rider2,'car',randint(1,100))
uber.find_a_vehicle(rider3,'car',randint(1,100))
uber.find_a_vehicle(rider4,'car',randint(1,100))
uber.find_a_vehicle(rider5,'car',randint(1,100))

print(rider1.get_trip_history())
