""" Chatbot:
   steps:
   1.input/listen
   2.process/decide
   3.output/talkback
 """
greet_words = ['hi','hello','yo','hey']
bye_words = ['bye','tata','hasta la vista']
bad_words = ['dog','pocha']

def listen():
    return input("Say Something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback("Hey Sir,How can I help you")
            break

        elif word in bye_words:
            talkback("Ta ta bro,Bye!")
            break
        elif word in bad_words:
            talkback("You are bad guy.Behave yourself")

def talkback(response):
    print(response)

while True:
    command = listen()
    decide(command)