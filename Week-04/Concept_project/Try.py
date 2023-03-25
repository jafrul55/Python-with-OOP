#classMethod and Static Method
class Text:
    def __init__(self,name):
        self.name = name

    
    @staticmethod  #it's will work as normal function
    def view(self1):
        # print(self)
        return self1
    
    @classmethod #class will received by parameter
    def view2(cls,name2):
        obj2 = cls(name2)
        # obj2 = Text(name2)

        return obj2
        

# obj = Text('Hello')
# obj.view('Hi')

# jafrul = Text.view('Hi')
# print(jafrul)

jaf = Text.view2('Jafrul')
print(jaf.name)

