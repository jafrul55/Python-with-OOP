#public protected private
class Account:
    def __init__(self,holder) -> None:
        self._account_holder = holder #(_account_holder)this is convension/protected

class StudentAccount(Account):
    def __init__(self,holder,balance,school):
        self.__balance = balance


    def withdraw(self,amount):
        if amount > self.__balance:
            return 'No money for you'
        self.__balance -= amount
        return amount

    def deposit(self,amount):
        if amount < 0:
            return 'Negative amount can not be added'
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
nas = StudentAccount('Nas Daily',12000,'Nas Academy')

# nas.__balance = 890000   #you can not set value live
nas.deposit(50000)   #you can deposite
nas.deposit(15000)
print(nas.get_balance())

# print(dir(nas))
# print(nas.__balance)
print(nas._StudentAccount__balance)

# _account_holder --> single underscore/protected(this everyone can understand)
#__balance --> you can not access