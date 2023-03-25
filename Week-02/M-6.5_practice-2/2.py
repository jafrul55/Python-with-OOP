import requests
import time
from win10toast import ToastNotifier

def get_activity():
    response = requests.get("http://www.boredapi.com/api/activity/")
    activity = response.json()['activity']
    return activity

toaster = ToastNotifier()

while True:
    activity = get_activity()
    toaster.show_toast("Bored? Try this!",activity,duration=10)
    time.sleep(1800) #Sleep for 30 minute (1800 seconds)