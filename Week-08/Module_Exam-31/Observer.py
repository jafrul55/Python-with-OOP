class ChatWithFriend:
    def __init__(self) -> None:
        self._Observer = []

    def attach(self,Observer):
        self._Observer.append(Observer)

    def detach(self,Observer):
        self._Observer.remove(Observer)

    def message_take_and_send(self,msg):
        self.notify(msg)

    def notify(self,msg):
        for message in self._Observer:
            message.update(msg)

class Observer:
    def __init__(self,name,background) -> None:
        self.name = name
        self.background = background

    def update(self,msg):
        print(f"Message for {self.name} who is {self.background} : {msg}")



Chat = ChatWithFriend()

Korim = Observer("Korim","Student")
Rohim = Observer('Rohim',"Army Soilder")
Akash = Observer("Akash","Police")
Jafrul = Observer("Jafrul","Software Engineer")

Chat.attach(Korim)
Chat.attach(Rohim)
Chat.attach(Akash)
Chat.attach(Jafrul)


Chat.message_take_and_send("Hello Guys,What's going on?")
Chat.message_take_and_send("Will you become a programmer?")

Chat.detach(Akash)
Chat.message_take_and_send("Hello Buddy,What'up?")  #Akash will be detach from the list
        