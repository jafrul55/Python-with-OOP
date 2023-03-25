import csv


class All_Airports:
    def __init__(self) -> None:
        self.load_airport_data('./data/airport.csv')
    
    def load_airport_data(self,file_path):
        with open(file_path,'r') as file:
            lines = csv.reader(file)
            
            for line in lines:
                print(line)

All_Airports()

