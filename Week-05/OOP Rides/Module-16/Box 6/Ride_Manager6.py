class RideManager:
    def __init__(self) -> None:
        print('Right manager activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []
 
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle_type)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle_type)
        else:
            self.__available_cngs.append(vehicle_type)
    
    def match_a_vehicles(self):
        pass


uber = RideManager()