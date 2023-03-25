import requests
import datetime

greet_words = ['hi','hello','yo','hey']
bye_words = ['bye','tata','take care']
bad_words = ['dog','scoundrel','stupid','ediate','idiot']
fine_words = ['fine','wonderful','mindblowing','joss','outstanding','brillient','talent','genious']

def listen():
    return input('Say Someting: ')

def get_activity():
    response = requests.get('http://www.boredapi.com/api/activity/')
    activity = response.json()['activity']
    return activity

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%p")
    return current_time

def decide(command):
    command = command.lower()
    broken_words = command.split(" ")


    for word in broken_words:
        if word in greet_words:
            talkback("Hi,How are you Boss")
        elif word in bye_words:
            talkback("Good Bye Boss!")
        elif word in bad_words:
            talkback("You are a bad boy")
        elif word in fine_words:
            talkback("Congress Boss.Best of Luck")
        elif 'bored' in command:
            activity = get_activity()
            talkback(f"You can try {activity}.")
            break
        elif 'time' in command:
            current_time = get_time()
            talkback(f"The current time is {current_time}.")
            break
        # else:
        #     talkback("I am sorry,I didn't understand that.")

def talkback(response):
    print(response)


while True:
    command = listen()
    decide(command)