class Account:
    def __init__(self,holder,initial_balance):
        self.holder = holder  #public attribute
        self._account_number = 165  #_(one underscore is a convension) because you can access and print
        self.__balance = initial_balance #__balance is a private attribute
        #you can not access from outside

    def deposit(self,amount):
        print(f'adding {amount} to your account')
        self.__balance += amount

    def withdraw(self,amount):
        print(f'withdrawing {amount} from your account')
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self,holder,initial_balance,school):
        self.school = school
        super().__init__(holder,initial_balance)

    def get_balance(self):
        # return self.__balance
        return self._account_number #you can also return


rafsan = StudentAccount('Rafsan',50000,'IUB')

# print(rafsan.__balance)
print(rafsan.holder)

rafsan.deposit(20000)
rafsan.deposit(35000)
rafsan.deposit(15000)
print(rafsan.get_balance())
# rafsan.__balance = 0
# print(rafsan.__balance)
rafsan._account_number = 135
print(rafsan._account_number)
