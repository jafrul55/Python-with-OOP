from abc import ABC, abstractmethod
#abstract base class(abc)
#Inforce you to do somthing
#abstract class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def name(self):
        pass
    @abstractmethod  #if you abstract then move method won't work
    def move(self):
        print('moving around in the zoo')

class Monkey(Animal):
    def sing(self):
        print('Monkey is singing')

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
    # you must define abstract methods any how in abstract class

layka = Monkey()
print(layka)
layka.eat()
layka.move()