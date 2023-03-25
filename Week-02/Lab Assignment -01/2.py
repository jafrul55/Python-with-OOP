import requests
import json
import time

def weather_data(api_key,City_name):
    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        # data = response.json()
        return data

api_key = input("Enter Your API Key: ") #api key:b09b579f44c76f6b427d548fdcfccdfe
City_name = input("Enter your City Name: ")
while True:
    Data = weather_data(api_key,City_name)
    print(Data)
    time.sleep(1800) #30 minutes convert to seconds
