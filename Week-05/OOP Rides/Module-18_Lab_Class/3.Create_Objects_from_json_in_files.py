import json
# class Item:
#     # all = []
#     def __init__(self,name,price) -> None:
#         self.name = name
#         self.price = price
        # self.all.append(self)

    # @staticmethod
    # def initialize(self):
    #     with open('extract.txt','r') as f:
    #         data = f.read()
    #         # print(data)
    #         js = json.loads(data)
            # print(js)
        #if you want to get value one by one:
#         for item in js:
#             print(item)


# item = Item('Jafrul',150)
# item.initialize()

#you can work with static mathod:
class Item:
    all = []
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
        self.all.append(self)

    @staticmethod
    def initialize():
        with open('extract.txt','r') as f:
            data = f.read()
            # print(data)
            js = json.loads(data)
            # print(js)
        #if you want to get value one by one:
        for item in js:
            Item(
                name = item["name"],
                price = item.get("price")
            )
    def __repr__(self) -> str:
        return f"Item({self.name},{self.price})"


Item.initialize()
print(Item.all)