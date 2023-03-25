# 4 Create airports from the loaded data:
import csv
from Airport5 import Airport
class All_Airports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airport_data('./data/airport.csv')
    
    def load_airport_data(self,file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        #get currency name <---> rate:
        with open('./data/currencyrates.csv','r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()

        #dictionary country <---> currency name:
        with open('./data/countrycurrency.csv','r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        #create airport
        with open(file_path,'r',encoding="utf8") as file:
            lines = csv.reader(file)
            
            try:
                for line in lines:
                    # print(line[4])
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)
            except KeyError as e:
                print(e)
            

            self.airports = airports
            for airport in airports.items():
                print(airport)

All_Airports()

