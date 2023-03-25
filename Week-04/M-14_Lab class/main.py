
#dimond ring problem:
class A:
    def print_somthing(self):
        print("Im on A")
class B(A):
    def print_somthing(self):
        print("Im on B")
class C(A):
    def print_somthing(self):
        print("Im on C")
class D(B,C):
    pass
#you can also use class D(B,C):

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_somthing()
obj2.print_somthing()
obj3.print_somthing()
obj4.print_somthing()