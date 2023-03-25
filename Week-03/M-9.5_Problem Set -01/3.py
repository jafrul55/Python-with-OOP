class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo",12,50)

# print(School_bus.capacity)
# print(School_bus.mileage)
# print(School_bus.name)

# print(type(School_bus))

print(isinstance(School_bus,Vehicle))
