import csv
from Aircraft import Aircraft

class Airlines:
    def __init__(self) -> None:
        self.aircrafts = None
        self.load_air_craft_data('./data/aircraft.csv')

    
    def load_air_craft_data(self,file_path):
        aircrafts = {}

        with open(file_path,'r') as file:
            lines = csv.reader(file)
            next(lines) #to skip header part
            for line in lines:
                # print(line)
                aircrafts[line[0]] = Aircraft(line[3],line[0],line[1],line[4])
        file.close()
        self.aircrafts = aircrafts

        for aircraft in aircrafts.items():
            # print(aircraft)
            pass

    def get_aircraft(self,code):
        return self.aircrafts[code]


val = Airlines()
value = val.get_aircraft("V22")
print(value)