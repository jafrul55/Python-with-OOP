#Single inheritance
#Multiple inheritance
#Multilevel inheritance

#Inheritance:
# class Parent:
#     def __init__(self) -> None:
#         self.string1 = "I am a parent"

# class Child(Parent):
#     def __init__(self) -> None:
#         self.string2 = "I am a child"
#         # super().__init__()
#         Parent.__init__(self)

# c = Child()
# print(c.string1)
# print(c.string2)

#Multiple Inheritance:
#if any class inherit to two class that is multiple inheritance
# class GrandParent:
#     def __init__(self) -> None:
#         self.string = "I am a grand parent"

# class Parent:
#     def __init__(self) -> None:
#         self.string = "I am a parent"

# class Child(Parent,GrandParent):
#     def __init__(self) -> None:
#         Parent.__init__(self)
#         GrandParent.__init__(self)
#         self.string = "I am a Child" #Under has most priority 


# C = Child()
# # print(C.string1)
# # print(C.string2)
# print(C.string)

#Multilevel Inheritance:
class GrandParent:
    def __init__(self) -> None:
        self.string = "I am a grand parent"

class Parent(GrandParent):
    def __init__(self) -> None:
        self.string = "I am a parent"
        super().__init__() #under possibility more

class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        # self.string = "I am a Child" #Under has most priority 


C = Child()
# print(C.string1)
# print(C.string2)
print(C.string)