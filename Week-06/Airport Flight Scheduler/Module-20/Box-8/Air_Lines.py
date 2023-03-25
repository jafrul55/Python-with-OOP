import csv
from Aircraft8 import Aircraft
class Airlines:
    def __init__(self) -> None:
        self.aircrafts = None
        self.load_air_craft_data('./data/aircraft.csv')
    
    def load_air_craft_data(self,csv_file):
        air_crafts = {}
        with open(csv_file,'r') as file:
            lines = csv.reader(file)
            # next(lines)
            for line in lines:
                # print(line)
                air_crafts[line[0]] = Aircraft(line[3],line[0],line[1],line[4])
        file.close()
        self.air_crafts = air_crafts

        # for air in air_crafts.items():
        #     print(air)
    
    def get_aircraft(self,code):
        return self.air_crafts[code]
Airlines()
      