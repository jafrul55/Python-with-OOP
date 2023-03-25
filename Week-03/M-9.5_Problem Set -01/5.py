class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name1 = name
        self.mileage1 = mileage
        self.capacity1 = capacity
    
    #getter method is @property
    #You can use @property.getter
    @property
    def name(self):
        return self.name1
    
    #setter method is @property_name.setter
    @name.setter
    def name(self,value):
        self.name1 = value
    
    #getter method is @property
    @property
    def mileage(self):
        return self.mileage1
    
    #setter method is @property_name.setter
    @mileage.setter
    def mileage(self,value):
        self.mileage1 = value


    #getter method is @property
    @property
    def capacity(self):
        return self.capacity1
    
    #setter method is @property_name.setter
    @capacity.setter
    def capacity(self,value):
        self.capacity1 = value
    

School_bus = Vehicle("School Volvo", 12, 50)
print(School_bus.name)

School_bus.name = 'Green Bird'
print(School_bus.name)

print(School_bus.mileage)
print(School_bus.capacity)
