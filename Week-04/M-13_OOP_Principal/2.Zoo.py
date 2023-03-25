from abc import ABC, abstractmethod
#abstract base class(abc)
#Inforce you to do somthing
#abstract class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def name(self):
        pass

    @abstractmethod  #if you abstract then move method won't work
    def move(self):
        print('moving around in the zoo')

class Monkey(Animal):
    #getter
    def __init__(self):
        self.__name = 'monkey'

    def sing(self):
        print('Monkey is singing')

    @property  #not call able
    def name(self):
        # return 'monkey'
        #getter
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    def eat(self):
        print('eating banana')

    def move(self):
        print('hanging on the branches of the trees')
        super().move()
# if you use here super() then it can print Animal move method

class Tiger(Animal):
    def eat(self):
        pass
    def move(self):
        pass
    # you must define abstract methods any how to call Tiger method

layka = Monkey()
print(layka)
layka.eat()
layka.move()

layka.name = 'moonkey'
#you can not call for @property
# print(layka.name()) 
#you can not call it as attribute
#so you should print as:
print(layka.name)

