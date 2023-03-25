class User:
    def __init__(self,name,password,phone):
        self.name = name
        self.__password = password #now password is private
        self.__phone = phone #it also private

    def __get_password(self):  #it also a private because of __
        print(self.__password)
    def user_login(self,name,password):
        if (name == self.name and password == self.__password):
            return True
        return False

ryan = User('Ryan Dal','NODEABCD','01925736849')
# print(ryan.__password)
# print(ryan.__phone)
# ryan.get_password()
result = ryan.user_login('Ryan Dal','NODEABCD')
print(result)