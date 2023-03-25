class Phone:
    manufactured = 'china' #Static
    def __init__(self,brand,price,color): #This is called instance/constructor
        self.brand = brand  #instance
        self.price = price
        self.color = color

    def send_sms(self,number,text):
        sms = f'sending: {text} to {number}'
        return sms
my_phone = Phone('oppo',13000,'black')
print(my_phone.brand,my_phone.manufactured)

her_phone = Phone('iphone',85000,'purple')
print(her_phone.brand,her_phone.manufactured)

dad_phone = Phone('Nokia',7000,'black')
print('My phone price:',my_phone.price,'Her phone price:',her_phone.price,'Dad phone price:',dad_phone.price)