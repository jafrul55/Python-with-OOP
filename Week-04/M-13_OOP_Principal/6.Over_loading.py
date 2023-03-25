#Method Overloading:
print(max(12,45,87,12,98,45,63,458,-8))
print(max([13,45,87]))
print(max('A','P','K','C'))

def add(num1,num2,num3=0,num4 = 0):
    return num1 + num2 + num3

# print(add(12,13))
# print(add(12,13,50))

def add2(*args,**kwargs):
    pass

#Operator Overloding:
# print(12 + 13)
# print('H' + 'W')

class Account:
    def __init__(self,holder,balance):
        self.holder = holder
        self.__balance = balance

    #Now you should use dunder Method:
    def __add__(self,other):  #dunder Method
        return self.__balance + other.__balance
    
    def __eq__(self, __o: object) -> bool: #dunder method
        return self.__balance == __o.__balance
        
my_account = Account('Sakib Al Hasan',50000)
her_account = Account('Shishir Vabi',90000)
result = my_account + her_account
print(result)

#this is called over_loading
