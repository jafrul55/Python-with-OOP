class Account:
    accID = 1
    def __init__(self,name,age,nid_num,balance):
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        #update Account:
        self.account_id = self.accID
        Account.accID +=1
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

account_1 = Account("Jafrul",23,600,500)
account_2 = Account("Kona",62,500,1000)

# print("1st one:",account_1.account_id)
# print("2nd one:",account_2.account_id)

print("Deposit: ")
account_1.deposit(2000)
account_2.deposit(200)
print("Account_1: ",account_1.balance)
print("Account_2: ",account_2.balance)


print("Withdraw: ")
account_1.withdraw(100)
account_2.withdraw(300)
print("Account_1: ",account_1.balance)
print("Account_2: ",account_2.balance)