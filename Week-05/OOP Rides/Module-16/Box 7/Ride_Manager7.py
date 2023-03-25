class RideManager:
    def __init__(self) -> None:
        print('Right manager activated')
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cngs = []
 
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cngs.append(vehicle)


    def get_available_vehicle_cars(self):
        return self.__available_cars

    def find_a_vehicle(self):
        pass


uber = RideManager()