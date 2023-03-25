# 2 Dynamic Attributes:

#Instance Attribute:
# class Item:
#     def __init__(self,ItemName,ItemPrice) -> None:
#         self.itemName = ItemName
#         self.itemPrice = ItemPrice

# item1 = Item("Bowl",100)
# item2 = Item("Plate",150)

# print(item1.__dict__)
# print(item2.__dict__)

#Class Attribute:
from tkinter import ALL


# class Item:
#     all = []
#     def __init__(self,ItemName,ItemPrice) -> None:
#         self.itemName = ItemName
#         self.itemPrice = ItemPrice
#         self.all.append(self)

#     def __repr__(self) -> str:
#         return f"Item({self.itemName},{self.itemPrice})"

# item1 = Item("Bowl",100)
# item2 = Item("Plate",150)

# print(item1.all)
# print(item2.all)

#Dynamic Attribute:
class Item:
    all = []
    def __init__(self,itemName,itemPrice) -> None:
        self.__itemName = itemName
        self.__itemPrice = itemPrice
        self.all.append(self)

    def __repr__(self) -> str:
        return f"Item({self.itemName},{self.itemPrice})"

item1 = Item("Bowl",100)
item2 = Item("Place",150)
item1._Item__discount = 10
item1._Item__itemName = "Bowl Broken"

# print(item1._Item__itemName)
# print(item1._discount)
# print(item1._Item__discount)


print(item1.__dict__)
        
        
