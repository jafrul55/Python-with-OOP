class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("Number of objects created: ",MyClass.count)