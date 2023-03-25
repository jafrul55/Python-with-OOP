#dunder
#magic method
#special method
class person:
    def __init__(self,name,age,money,height = 65):
        self.name = name
        self.age = age
        self.money = money
        self.height = height
    
    def __call__(self):
        print(f'This is {self.name} with age {self.age} and have {self.money}')

    def __eq__(self,other):
        return self.age == other.age
    
    def __len__(self):
        return self.height
    
    def __repr__(self) -> str:  #__repr__ function is used to represent the as string
        return f'Name: {self.name} age: {self.age} money: {self.money}'
    
    def __add__(self,other):  #__add__ function is use to add two operator
        # return self.money + other.money
        return self.age + other.age
    
alim = person('Alim',15,560)
dalim = person('Dalim',16,715)

print(alim + dalim)

# print(type(alim))

alim()

print('compare two objects:',alim == dalim)

print(len(alim))
print(dalim)

