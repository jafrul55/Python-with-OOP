class Vehicle:
    wheels = 4  # class property
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    
    @classmethod
    def get_wheels(cls):
        return cls.wheels
    

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo",12,50)

print(Vehicle.get_wheels())

print(School_bus.get_wheels())



