#Instance method
#Static method
#Class method
#Abstract method

#Instance method:
# class School:
#     school_name = 'ABC School' #class variable
#     def __init__(self,name) -> None: #self for object
#         self.name = name #name is instance variable
    
#     def printname(self):
#         print(self.name)

#     def change_name(self,name):
#         self.school_name = name
        

#     @classmethod
#     def get_name(cls):  #cls for classmethod
#         cls.school_name = "ABCD SCHOOL"
#         print(cls.school_name)
# #Class Method can not access instance method

#     @classmethod
#     def change_school_name(cls):
#         cls.school_name = "ABCD School"

# s1 = School('Jafrul')
# s2 = School('Tusar')
# s1.change_name('Ideal School')
# val.printname()
# School().get_name()
# print(s1.school_name)

#this can not change school
# print(s2.school_name)

#but this can change school name
# School.change_school_name()
# print(s2.school_name)

""" 
we learn:
1.class method can change,update,access to update variable.
2.class method can not access or modify instance method.
2.instance method can not change,update,access to class variable
"""
# Static Method:

class School:
    school_name = 'ABC School' #class variable
    def __init__(self,name) -> None: #self for object
        self.name = name #name is instance variable
    
    def printname(self):
        print(self.name)

    def change_name(self,name):
        self.school_name = name

    @classmethod
    def change_school_name(cls):
        cls.school_name = "ABCD School"

    @staticmethod
    def greet():
        print("Hello Students")

s1 = School('Jafrul')
s2 = School('Tusar')

# School.greet()


""" 
Static Method:
1.It can not access cls of class.
2.Staticmethod is a normal function.
"""

#Abstract class / Method:

"""
1.When we want to "blue print" of the class that time we use
Abstract Class.
2.We cannot create an object of abstract class
3.When we want to make blue print for any house
"""
from abc import ABC,abstractmethod
#we use it sothat it can not print object of abstract class
class Vehicle(ABC): 
    @abstractmethod
    def go(self):
        print("This is an abstract Class")

# Can't instantiate abstract class Car with abstract method stop   
    @abstractmethod
    def stop(self):
        pass

#so we must need to write "stop method" incase of Car and Bike class to run code
class Car(Vehicle):
    def go(self):
        print("I am car")
    def stop(self):
        print("Print Car")

class Bike(Vehicle):
    def go(self):
        print("I am Motor Bike")

    def stop(self):
        print("print Motor Bike")

# c = Vehicle()
# c.go()

CAR = Car()
CAR.go()

MotorBike = Bike()
MotorBike.go()
# Can't instantiate abstract class Vehicle with abstract method go 

        

