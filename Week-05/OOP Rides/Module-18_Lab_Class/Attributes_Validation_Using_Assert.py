# 1 Attributes Validation Using Assert:


# class Item:
#     def __init__(self,itemName,itemPrice) -> None:
#         assert itemPrice >= 0,f"Error line 3, {itemPrice} is invalid"
#         self.itemName = itemName
#         self.itemPrice = itemPrice

# item = Item("Plate",-150)
# print(item.itemName, item.itemPrice)




class Person:
    def __init__(self,name,phone,age) -> None:
        assert age > 13,f"Only greater than 13 is accepted"
        assert len(phone) == 11, f"Invalid phone no"
        self.name = name
        self.phone = phone
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} {self.phone} {self.age}"


user = Person("Jafrul","01925736849",114)
# if i give wrong phone_no or age:
# user = Person("Jafrul","01925736849",13)
# user = Person("Jafrul","0192573684",14)

print(user)





        