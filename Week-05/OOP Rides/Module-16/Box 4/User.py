# Create License Check authority:
import hashlib
from unittest import result
from brta import BRTA

license_authority = BRTA()
class User:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        pwd_encrypt = hashlib.md5(password.encode()).hexdigest()
        with open('Users.txt','w') as file:
            file.write(f'{email} {pwd_encrypt}')
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

    def start_a_trip(self,destination,fare):
        self.earning += fare
        self.location = destination

Hero = User("Hero Alom","hero@alom.com",'heroOhAlaom')
User.log_in("hero@alom.com",'heroOhAlaom')

Kuber = Driver('Kuber Maji','Kuber@maji.com','Kopilajaisna',54,4556)

result = license_authority.validate_license(Kuber.email,Kuber.license)
print(result)
Kuber.take_driving_test()
result = license_authority.validate_license(Kuber.email,Kuber.license)
print(result)