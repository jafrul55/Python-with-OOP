class Vehicle:
    def __init__(self,name,license,price):
        self.name = name
        self.license = license
        self.price = price
        print('Vehicle class init called')

    def start(self):
        print(f'{self.name} started')

class Bus(Vehicle):
    def __init__(self,name,license,price,seat,ticket_price):
        self.seat = seat
        self.available_seats = seat
        self.ticket_price = ticket_price
        print('Bus init called')
        # upper level __init__ call
        super().__init__(name,license,price)

    def sell_ticket(self,customer_name,quantity,amount):
        self.available_seats -= quantity
        remainder = amount - self.ticket_price * quantity
        if remainder >= 0:
            return Ticket(customer_name)
        return 'no ticket for you'
    
class ACBus(Bus):
    def __init__(self):
        print('AC bus created')

class MiniBus(Bus):
    def __init__(self):
        print('mini bus created')
        #upper level __init__ call
        super().__init__('Mimi Mimi','DKA125',1200000,50,450)
        # you can also use this instead of super()
        # Bus.__init__(self,'Mimi Mimi','DKA125',1200000,50,450)

        # you can also call user function
        # super().sell_ticket('Bappa',1,1000)

    
class Ticket:
    def __init__(self,owner) -> None:
        self.owner = owner

mini = MiniBus()
print(mini.name)
print(mini.seat)
print(mini.available_seats)

