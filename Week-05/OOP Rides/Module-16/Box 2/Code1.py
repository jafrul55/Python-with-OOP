#  Create User with password verification:
import hashlib
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
        print('Password found: ',store_password)
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == store_password:
            print('Valid User')
            return True
        else:
            print('Invalid User')
            return False


Hero = User("Hero Alom","hero@alom.com",'heroOhAlaom')
User.log_in("hero@alom.com",'heroOhAlaom') 